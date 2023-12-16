import pandas as pd
import streamlit as st

import src.answers as asw
from src.extraction import load_data

st.set_page_config(
    page_title='Sections - Database Description',
    page_icon=':bar_chart:',
    layout='wide'
)

def create_dataframe_section(df):
    st.write('# :bar_chart:  Sections - Database Description')
    st.divider()

    col1, col2 = st.columns(2, gap='large')

    col1.header("Database:")
    col1.dataframe(df, height=545)

    col2.header("Data Description:")

    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos por mês |
                        | company | Fabricanete da Motocicleta |
    """

    col2.markdown(data_description)
    st.subheader('', divider='gray')

def create_answers_section(df):
    st.write("# :feather: Main Questions Answers")
    st.subheader('', divider='gray')

    st.header("First Round:")
    st.subheader(
        "1. How many bikes are being sold by their owners and how many bikes are being sold by distributors?"
    )
    asw.rd1_question_9(df)
    st.subheader('', divider='gray')

    st.subheader("2. How many bikes are being sold are bikes from a unique owner?")
    asw.rd1_question_13(df)
    st.subheader('', divider='gray')

    st.subheader(
        "3. Are high kilometer bikes more expensive than bikes with lower kilometer?"
    )
    asw.rd1_question_14(df)
    st.subheader('', divider='gray')

    st.subheader(
        "4. Are the bikes with a unique owner more expense on avarege than the other bikes?"
    )
    asw.rd2_question_1(df)
    st.subheader('', divider='gray')

    st.subheader(
        "5. Are the bikes that have more owners also the bikes with more kilometers traveled on avarege?"
    )
    asw.rd2_question_2(df)
    st.subheader('', divider='gray')

    st.subheader("6. Which company has the most bikes registered?")
    asw.rd2_question_7(df)
    st.subheader('', divider='gray')

    st.subheader("7. Which company has the most expensive bikes on avarege?")
    asw.rd3_question_2(df)
    st.subheader('', divider='gray')

    st.subheader(
        "8. Are the company that has the most expensive bikes registered also the company with the most bikes registered?"
    )
    asw.rd3_question_5(df)
    st.subheader('', divider='gray')

    st.subheader("9. Which bikes are good for buying?")
    asw.rd3_question_7(df)
    st.subheader('', divider='gray')
    st.markdown('###### Powered by Pedro Castro | papodeds®')

def utils(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df

def create_main_layout():
    df = load_data()

    df = utils(df)

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()
