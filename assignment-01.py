def adv_print(text, start='', max_line=120, in_file=False):
    if in_file is True:
        with open('adv_file.txt', 'w', encoding='UTF-8') as f:
            f.write(text)
    i = 0
    step = max_line
    while i < len(text):
        print(f'{start}{text[i:max_line]}')
        i += step
        max_line += step


adv_print(text='The Count of Monte Cristo by Alexander Dumas')

adv_print(text='The novel opens in 1815 as the Pharaon arrives in Marseille. The ship’s owner, Monsieur Morrel, '
               'learns from the young first mate, Edmond Dantès, that the captain died on the journey and that Dantès '
               'took over. The ship’s accountant, Danglars, is bothered that the Pharaon stopped at Elba, but Dantès '
               'explains that the captain left a package to be delivered to one of Napoleon’s marshals who is in '
               'exile with Napoleon on the island. Morrel makes Dantès captain of the ship, to Danglars’s '
               'displeasure. On visiting his father, Dantès learns that a neighbour, Gaspard Caderousse, took most of '
               'his father’s resources in payment of a debt. Dantès then goes to see his fiancée, Mercédès, '
               'and finds her in the company of Fernand Mondego, who is in love with her. After leaving, '
               'Mondego encounters Danglars and Caderousse, and a decision is made to falsely accuse Dantès of '
               'treason. In a letter to the crown prosecutor, Danglars alleges that Dantès is a Bonapartist and is '
               'carrying a letter from Napoleon to the Bonapartist committee in Paris.', start='^', in_file=True,
          max_line=90)
