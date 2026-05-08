import plotly.graph_objects as go
data = {'Min Latency':45.35,'Max Latency':45.94,'Avg Latency':45.83,'Throughput':400.6,'Total Transaction':1500,'Test Load':500,'Block Finality':2035.07}
categories = list(data.keys())
values = [data['Min Latency'],data['Max Latency'],data['Avg Latency'],data['Throughput'],data['Total Transaction']/10,data['Test Load'],data['Block Finality']/10]
fig = go.Figure(go.Scatterpolar(r=values,theta=categories,fill='toself',line_color='teal'))
fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0,500])),title="Adversarial AI In Medical Imaging Metrics")
fig.write_html("my_chart.html")
fig.show()
