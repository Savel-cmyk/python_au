import sys

class LeetCodeSource:
    def __init__(self, title, link, code):
        self.title = title.rstrip('\n').split('. ')[1]
        self.link = link.rstrip('\n')
        self.code = code

    def get_md_formatted_code(self):
        return '```python\n{}\n```'.format('\n'.join(map(lambda x: x.rstrip('\n'), self.code)))

    def get_md_title(self):
        return '## {}'.format(self.title)

    def get_md_solution_link(self):
        return '+ [{}](#{})'.format(self.title, self.link[-6:-1])

    def get_md_formatted_solution(self):
        return (self.get_md_solution_link(), '{}\n\n{}\n\n{}'.format(self.get_md_title(), self.link, self.get_md_formatted_code()))

def read_all_lines_from_file(file_name):
    file = open(file_name, 'r')
    result = file.readlines()
    file.close()
    return result

def write_to_md(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

def read_all_file(file_name):
    file = open(file_name, 'r')
    result = file.read()
    file.close()
    return result

def merge_solutions(old_solution, new_solution, emerged_link):
    old_splitted = old_solution.split('\n\n')
    if len(old_splitted) == 1:
        return '# Math\n\n{}'.format('\n\n'.join(map(lambda x: x, [emerged_link, new_solution])))
    return '{}\n{}\n\n{}\n\n{}'.format('\n\n'.join(old_splitted[:2]), emerged_link, '\n\n'.join(old_splitted[2:]), new_solution)

def main(src, dst):
    in_text = read_all_lines_from_file(src)
    x = LeetCodeSource(in_text[0], in_text[1], in_text[2:])
    emerged_links, new_solutions = x.get_md_formatted_solution()
    old_solutions = read_all_file(dst)
    result = merge_solutions(old_solutions, new_solutions, emerged_links)
    write_to_md(dst, result)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
