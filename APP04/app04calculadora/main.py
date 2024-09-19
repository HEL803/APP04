import flet as ft

def calc_suma(txtnum1,txtnum2,lblresultado)
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1+num2
        lblresultado.value="resultado:{resultado}"
    except ValueError:
        lblresultado.value="error ingresa valores correctos"
            


def main(page: ft.Page):
    page.title="calculadora"
    page.bgcolor="yellow"
    
    txtnum1=ft.TextField(label="ingresa el primer numero",color=green)
    txtnum2=ft.TextField(label=" ingresa el segundo numero",color="yellow")
    lblresultado=ft.Text("resultado:",color="green")
    
    btnsuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnresta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnmulti=ft.ElevatedButton(text="*",on_click=on_calc_multi)
    btndiv=ft.ElevatedButton(text="/",on_click=on_calc_div)
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtnum1,
                txtnum2
            ],aligmnent="center" ),
        ]),
        ft.Row(controls=[lblresultado],aligment="center")
        ft.Row(controls=[
            btnsuma,
            btnresta,
            btnmulti,
            btndiv  
        ],aligment="center")
    )


ft.app(main)
