class Config(object):
    dorks = {
        'directory_listing': 'https://www.google.com/search?q=site:{}+intitle:index.of&hl=en',

        'configuration_files': 'https://www.google.com/search?q=site:{}+ext:xml+|+ext:conf+|+'
                               'ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+e'
                               'xt:ora+|+ext:ini&hl=en',

        'database_files': 'https://www.google.com/search?q=site:{}+ext:sql+|+ext:dbf+|+ext:md'
                          'b&hl=en',

        'log_files': 'https://www.google.com/search?q=site:{}+ext:log&hl=en',

        'backup_and_old_files': 'https://www.google.com/search?q=site:{}+ext:bkf+|+ext:bkp+|+e'
                                'xt:bak+|+ext:old+|+ext:backup&hl=en',

        'login_pages': 'https://www.google.com/search?q=site:{}+inurl:login&hl=en',

        'sql_errors': 'https://www.google.com/search?q=site:{}+intext:%22sql+syntax+near%22+|+i'
                      'ntext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%'
                      '22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mys'
                      'ql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warnin'
                      'g:+pg_connect()%22&hl=en',

        'publicly_exposed_documents': 'https://www.google.com/search?q=site:{}+ext:doc+|+ext:do'
                                      'cx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+e'
                                      'xt:ppt+|+ext:pptx+|+ext:pps+|+ext:csv&hl=en',

        'php_info': 'https://www.google.com/search?q=site:{}+ext:php+intitle:phpinfo+%22publish'
                    'ed+by+the+PHP+Group%22&hl=en'
    }
    min_delay = 5
    max_delay = 10
    user_agents = [
        {
            'name': 'Windows 10-based PC using Edge browser',
            'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
        },
        {
            'name': 'Chrome OS-based laptop using Chrome browser (Chromebook)',
            'value': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
        },
        {
            'name': 'Mac OS X-based computer using a Safari browser',
            'value': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 '
                     '(KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
        },
        {
            'name': 'Windows 7-based PC using a Chrome browser',
            'value': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/47.0.2526.111 Safari/537.36'
        },
        {
            'name': 'Linux-based PC using a Firefox browser',
            'value': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
        }
    ]

    headers = [
        {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
                      ';q=0.8,application/signed-exchange;v=b3;q=0.9',
            
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': user_agents[0]['value']
        },
        {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
                      ';q=0.8,application/signed-exchange;v=b3;q=0.9',
            
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': user_agents[1]['value']
        },
        {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
                      ';q=0.8,application/signed-exchange;v=b3;q=0.9',
            
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': user_agents[2]['value']
        },
        {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
                      ';q=0.8,application/signed-exchange;v=b3;q=0.9',
            
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': user_agents[3]['value']
        },
        {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
                      ';q=0.8,application/signed-exchange;v=b3;q=0.9',
            
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': user_agents[4]['value']
        },
    ]
