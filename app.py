from nicegui import ui
import plotly.graph_objects as go


class Demo: 
    def __init__(self): 
        self.number = 1

ui.label("Hola, NiceGUI")
ui.icon("lock")
ui.icon("apps",color="gray",size="50px") 

ui.avatar('adb',text_color='green', square=True,color='yellow',size="50px") 
ui.link("The best Computer Science Portal","https://www.geeksforgeeks.org/") 
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')

ui.label('CSS').style('color: #888; font-weight: bold; background-color: yellow;')
ui.label('Tailwind').classes('uppercase; underline')
ui.label('Quasarsss').classes('text-h3')

ui.button('Button', on_click=lambda: ui.notify('Click'))

toggle1 = ui.toggle([1, 2, 3], value=1)

switch = ui.switch('switch me')
ui.label('Switch!').bind_visibility_from(switch, 'value')

slider = ui.slider(min=0, max=100, value=50)
ui.label().bind_text_from(slider, 'value')

fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 2.5]))
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
ui.plotly(fig).classes('w-full h-40')

ui.run(native=True, window_size=(400, 300), fullscreen=False)