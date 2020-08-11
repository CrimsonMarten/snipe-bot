#! /usr/bin/python3

import aiohttp, bs4

async def scrape(crn):
    """
    Return all registration data in a list as [s_cap, s_act, s_rem, w_cap, w_act, w_rem]

    Keyword arguments:
    crn -- CRN for the class
    """
    # Download class information using CRN
    url = 'https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=202008&crn_in=' + crn

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # Download source code
            oscar_soup = bs4.BeautifulSoup(await resp.text(), features='html.parser')

            # Parse HTML for registration data
            reg_table = oscar_soup.find('caption', string='Registration Availability').find_parent('table')

            if len(reg_table) == 0:
                raise ValueError()

            reg_data = [int(x.getText()) for x in reg_table.findAll('td', class_='dddefault')]
            return reg_data


async def class_status(reg_data):
    """
    Returns class registration status, that is, "Open", "Open Waitlist", "Closed".

    Keyword arguments:
    reg_data -- list containing registration data obtained from oscar_scraper() function
    """

    s_cap, s_act, s_rem, w_cap, w_act, w_rem = reg_data

    if w_cap > 0:
        return "Open Waitlist" if w_rem > 0 else "Closed"
    elif s_rem > 0:
        return "Open"
    else:
        return "Closed"
 