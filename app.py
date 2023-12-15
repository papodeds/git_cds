import streamlit as st 
from src.extraction import load_data

st.set_page_config(layout='wide')

def create_dataframe_section(df):
    st.title('Database Section')

    col1, col2 = st.columns(2)

    col1.header('Database')
    col1.dataframe(df, height=530)

    col2.header('Data Description')

    data_description =  """
                         | Coluna | Descrição |
                         | : -----|---------: |
                         | ID | Identificador da linha/registro |
                         | name | Fabricante e Modelo da Moto |
                         | selling_price | Preço de Venda |
                         | year | Ano de Fabricação da Moto |
                         | seller_type | Tipo de vendedor - Se é vendedor pessoal ou revendedor |
                         | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                         | km_driven | Quantidade de Quilometros percorrido pela moto |
                         | ex_showroon_price | Preço da motocicleta sem as taxas de seguro e registro |
                         | age | Quantidade de anos em que a moto está em uso |
                         | km_class | Classificação das motos conforme a quilometragem percorrida |
                         | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                         | Km_per_month | Quantidade de Quilometros percorridos por mês |
                         | company | Fabricante da Motocicleta |
                        """
    
    col2.markdown(data_description) 

    return None
    
def create_answers_section(df):
     st.title('Main Questions Answers')
     st.header('First Round')

     st.subheader('How many bikes are being sold by their owners and how many bikes are being sold by distributors?')
     st.subheader('How many bikes are being sold are bikes from a unique owner?')
     st.subheader('Are high kilometer bikes more expensive than bikes with lower kilometer?')
     st.subheader('Are the bikes with a unique owner more expense on avarege than the other bikes?')
     st.subheader('Are the bikes that have more owners also the bikes with more kilometers traveled on avarege?')
     st.subheader('Which company has the most bikes registered?')
     st.subheader('Wiche company has the most expensive bikes on avarege?')
     st.subheader('Are the company thta has the most expensive bikes registered also the company with the most bikes registered?')
     st.subheader('Which bikes are good for buying?')

     return None

def main():
    df = load_data()
    create_dataframe_section(df)
    create_answers_section(df)
    st.dataframe(df)

if __name__ == '__main__':
        main()
