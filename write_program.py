import re


def main():
    # Read-file vars
    read_file = open('tautulli.txt', 'r')
    file_text = read_file.read()
    # Write-file vars
    # write_file = open('tautulli.py', 'a')
    # Regex patterns
    full_pat = re.compile(
        r'^\s{4}def\s(?P<m_name>\w+?)\(self.*?\):.*?'
        r'(?P<doc_string>""".*?""")$',
        re.MULTILINE.DOTALL
    )
    m_name_pat = re.compile(
        r'def\s(?P<m_name>\w+?)\(self'
    )
    kv_pat = re.compile(
        r'\(self(,\s)?(?P<kv>\w+?=.+?)(,\s+|\):)',
        re.MULTILINE
    )
    arg_pat = re.compile(r',\s+(?P<arg>\w+?)=')
    val_pat = re.compile(r'\w+?=(?P<val>.+)(,\s|\):)')
    doc_pat = re.compile(r'(?P<doc_string>""".*?""")')

    start_def_str = '\n    def '

    print(full_pat.match(file_text))
    # for i in full_pat.finditer(file_text):
    #     print(i)

    read_file.close()


if __name__ == '__main__':
    main()
