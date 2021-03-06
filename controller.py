import requests
from config import DEFAULT_CONFIG, question_content_query_template
from helper import *
from bs4 import BeautifulSoup
import pystache
import json
import time
import re


class Controller:
    def __init__(self, session, update_all=False):
        self.session = session
        self.update_all = update_all
        self.processed_list = self.load_processed_list()
        self.data = {}
        self.headers = {}
        self.user = {}
        self.pattern = re.compile(r"submissionCode:\s*'([\s\S]*)',\s*editCodeUrl")

    def load_processed_list(self):
        res = []
        try:
            with open('{}/result.json'.format(get_solution_dir()), 'r') as f:
                tmp = json.load(f)
            if tmp is not None:
                res = [int(key) for key in tmp.keys() if key.isdigit()]
        except:
            pass
        return res

    def make_options(self, url):
        options = {'url': url, 'headers': {'Referer': DEFAULT_CONFIG['sys']['urls']['base']}}
        return options

    def signin(self, user):
        headers = {
            'Referer': DEFAULT_CONFIG['sys']['urls']['base'], 'Accept-Encoding': '',
            'Connection': 'close'}
        req = self.session.get(DEFAULT_CONFIG['sys']['urls']['login'], headers=headers)
        user['loginCSRF'] = req.cookies.get('csrftoken')
        payloads = {
            'csrfmiddlewaretoken': user['loginCSRF'],
            'login': user['login'],
            'password': user['pass']
        }
        self.session.post(DEFAULT_CONFIG['sys']['urls']['login'], payloads, headers=headers)
        self.headers = headers
        self.user = user

    def get_user(self):
        return self.user

    def get_headers(self):
        return self.headers

    def fetch_ac_lists(self):
        user = self.get_user()
        headers = self.get_headers()
        req = self.session.get(DEFAULT_CONFIG['sys']['urls']['algorithm'], headers=headers)
        data = req.json()
        self.data['total'] = data['num_total']
        self.data['solved'] = data['num_solved']
        self.data['locked'] = 0
        self.data['language'] = 'python3'
        return data['stat_status_pairs']

    def fetch_solutions(self, ac_list):
        result = {}
        elements = []
        for element in ac_list:
            if element['paid_only']:
                self.data['locked'] += 1
            if element['status'] == 'ac' and element['stat']['question_id'] not in result and element['stat']['question_id'] not in self.processed_list:
                elements.append(element)
        return elements

    def fetch_all(self, ac_list):
        language_code_map_arr = []
        if ac_list and len(ac_list) > 0:
            for ac_problem in ac_list:
                language_clone = []
                language_code_map = {'title': ac_problem['stat']['question__title_slug'],
                                     'id': ac_problem['stat']['question_id'],
                                     'level': ac_problem['difficulty']['level'], 'paid_only': ac_problem['paid_only'],
                                     'acceptance': '{:.2f}%'.format(
                                         ac_problem['stat']['total_acs'] / ac_problem['stat'][
                                             'total_submitted'] * 100)}
                for language in DEFAULT_CONFIG['sys']['langs']:
                    language_clone.append(language)
                self.fetch_and_write(ac_problem, language_clone, language_code_map)
                time.sleep(3)
                language_code_map_arr.append(language_code_map)
        if len(language_code_map_arr) > 0:
            self.write_result(language_code_map_arr, get_solution_dir())
            self.generate_markdown()

    def fetch_and_write(self, ac_problem, language_clone, language_code_map):
        self.fetch_ac_solution_of_problem(ac_problem, language_clone, 0, language_code_map)
        self.fetch_question(ac_problem, language_code_map)
        self.write_to_file(language_code_map, get_solution_dir())
        return language_code_map

    def fetch_ac_solution_of_problem(self, problem_info, language_to_fetch, page, language_code_map):
        if len(language_to_fetch) < 1:
            return language_code_map
        url = '{}{}/?offset={}&limit=20'.format(DEFAULT_CONFIG['sys']['urls']['solution'], problem_info['stat']['question__title_slug'], page * 20)        
        headers = self.headers
        headers['Accept'] = '*/*'
        req = self.session.get(url, headers=headers)
        submission_json = req.json()['submissions_dump']
        submission_json = sorted(submission_json, key=lambda e:e.__getitem__('id'), reverse=True)
        for element in submission_json:
            if element['status_display'] != 'Accepted':
                continue
            code_url = element['url']
            req = self.session.get(DEFAULT_CONFIG['sys']['urls']['base']+code_url)
            match_result = self.pattern.findall(req.text)
            code = eval("'" + match_result[0] + "'")
            language_code_map['python'] = code
            if element['status_display'] == 'Accepted':
                break
        return language_code_map

    def fetch_question(self, problem_info, language_code_map):
        url = DEFAULT_CONFIG['sys']['urls']['graphql']
        payloads = question_content_query_template
        payloads['variables']['titleSlug'] = problem_info['stat']['question__title_slug']
        headers = self.headers
        req = self.session.post(url, json=payloads, headers=headers)
        question_json = req.json()
        question = question_json['data']['question']['content']
        language_code_map['question'] = question
        return language_code_map

    def write_to_file(self, language_code_map, solutions_dir_path):
        output_path = '{}/{}.{}'.format(solutions_dir_path, format_id(language_code_map['id']), language_code_map['title'])
        mkdir(output_path)
        with open('{}/{}.{}'.format(output_path, language_code_map['title'], 'py'), 'w') as f:
            f.write(language_code_map['python'])
        with open('{}/question.md'.format(output_path), 'w') as f:
            f.write(language_code_map['question'])

    def write_result(self, language_code_map_arr, result_json_path):
        with open('{}/result.json'.format(result_json_path), 'r') as f:
            result = json.load(f)
        if result is None:
            result = {}
        for element in language_code_map_arr:
            ele = {'id': element['id'], 'level': element['level'], 'title': element['title'],
                   'paid_only': element['paid_only'], 'acceptance': element['acceptance'],
                   'language': 'python3'}
            result[str(element['id'])] = ele
        result['last_update_time'] = time.strftime('%Y-%m-%d', time.localtime())
        result['total'] = self.data['total']
        result['solved'] = self.data['solved']
        result['locked'] = self.data['locked']
        result['language'] = self.data['language']
        with open('{}/result.json'.format(result_json_path), 'w') as f:
            json.dump(result, f)

    def generate_markdown(self):
        with open('{}/result.json'.format(get_solution_dir()), 'r') as f:
            result_object = json.load(f)
        template_path = get_resource_file('README.tpl')
        tpl = self.read_and_copy_tpl(template_path)
        output_dir = get_solution_dir()
        hard_cnt = 0
        medium_cnt = 0
        easy_cnt = 0
        problem_numbers = []
        for key in result_object.keys():
            if isinstance(key, str) and key.isdigit():
                problem_numbers.append(key)
        solutions = []
        for num in problem_numbers:
            id_str = format_id(num)
            difficulty = result_object[num]['level']
            if difficulty == 1:
                easy_cnt += 1
                difficulty_char = 'Easy'
            elif difficulty == 2:
                medium_cnt += 1
                difficulty_char = 'Medium'
            elif difficulty == 3:
                hard_cnt += 1
                difficulty_char = 'Hard'
            solution_links = '[{}](./{}/{}.{}/{}.{})'.format('python3',
                                                            output_dir,
                                                            id_str,
                                                            result_object[num]['title'],
                                                            result_object[num]['title'],
                                                            'py')
            solutions.append({
                'id': id_str,
                'title': result_object[num]['title'],
                'solution_link': solution_links,
                'difficulty': difficulty_char,
                'paid_only': ':heavy_check_mark:' if result_object[num]['paid_only'] else '',
                'acceptance': result_object[num]['acceptance']
            })
        solutions.sort(key=lambda x: int(x['id']))
        view_data = {
            'language': 'python3',
            'total': self.data['total'],
            'solved': self.data['solved'],
            'locked': self.data['locked'],
            'hard': hard_cnt,
            'medium': medium_cnt,
            'easy': easy_cnt,
            'time': time.strftime('%Y-%m-%d', time.localtime()),
            'solutions': solutions
        }
        content = pystache.render(tpl, view_data)
        with open('README.md', 'w') as f:
            f.write(content)

    def read_and_copy_tpl(self, local_tpl_path):
        with open(local_tpl_path, 'r', encoding='utf-8') as f:
            return f.read()

    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    session = requests.Session()
    controller = Controller(session)
    user = {
        'login': 'zhipenghao930930@gmail.com',
        'pass': 'peqxe4-jihtez-noVwez'
    }
    controller.signin(user)
    ac_list = controller.fetch_ac_lists()
    solutions = controller.fetch_solutions(ac_list)
    controller.fetch_all(solutions)
    controller.close_session()
