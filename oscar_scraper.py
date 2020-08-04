import requests, bs4

def scrape(crn):
    """
    Return all registration data in a list as [s_cap, s_act, s_rem, w_cap, w_act, w_rem]

    Keyword arguments:
    crn -- CRN for the class
    """
    # Download class information using CRN
    url = 'https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=202008&crn_in=' + crn
    res = requests.get(url)
    res.raise_for_status()

    # Download source code
    oscar_soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # Parse HTML for registration data
    reg_table = oscar_soup.find('caption', string='Registration Availability').find_parent('table')
    reg_data = [int(x.getText()) for x in reg_table.findAll('td', class_='dddefault')]
    return reg_data
    