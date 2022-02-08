import streamlit as st
from random import randint
from data import main_meaning, action, for_what, for_whom


adding_idea_4 = randint(0, 1)
idea_1 = main_meaning[randint(0, len(main_meaning) - 1)]
idea_2 = action[randint(0, len(action) - 1)]
idea_3 = for_whom[randint(0, len(for_whom) - 1)]
idea_4 = for_what[randint(0, len(for_what) - 1)]
idea = ''

st.title('Генератор идей для хакатона.')
st.write('Не знаете, с чего начать? Мозговой штурм не даёт успеха? Наш генератор идей для хакатона как минимум '
         'повеселит Вас, но и вполне возможно, что вы получите вдохновение и новую идею!')
button1 = st.button('Сгенерировать идею!')

if button1:
    if idea_1 == 'Генератор ' or idea_1 == 'Русификатор ':
        if adding_idea_4 == 1:
            st.write(idea_1 + idea_3 + idea_4)
        else:
            st.write(idea_1 + idea_3)
    else:
        if adding_idea_4 == 1:
            st.write(idea_1 + idea_2 + idea_3 + idea_4)
        else:
            st.write(idea_1 + idea_2 + idea_3)
