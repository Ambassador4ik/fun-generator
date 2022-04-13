import string
import translator as tr
import generator as g
import seed as s
import stats_collector as stats

count = 0
while True:
    count += 1
    st = tr.translate(g.generate_random())
    lines = st.split(' ')
    for i in range(len(lines)):
        lines[i] = lines[i].translate(str.maketrans('', '', string.punctuation))
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()

    stats.collect(lines)
    print('Collected stats from', count, 'texts')
