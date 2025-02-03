import os
import datapane as dp
import pandas as pd

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "wow_demographics.csv")
df = pd.read_csv(csv_path)
data_table = dp.DataTable(df)
table = dp.Table(df)
grouped_by_gender = df.groupby(['Gender']).size().reset_index(name='Count')
bar_plot_gender = grouped_by_gender.plot.bar(x='Gender', y='Count', title="Distribución por Género")
bar_plot_gender_dp = dp.Plot(bar_plot_gender)
grouped_by_faction = df.groupby(['Faction']).size().reset_index(name='Count')
pie_plot_faction = grouped_by_faction.plot.pie(y='Count', labels=grouped_by_faction['Faction'], legend=False, ylabel="", title="Distribución por Facción")
pie_plot_faction_dp = dp.Plot(pie_plot_faction)
grouped_by_role = df.groupby(['Role']).size().reset_index(name='Count')
bar_plot_role = grouped_by_role.plot.bar(x='Role', y='Count', title="Distribución por Rol")
bar_plot_role_dp = dp.Plot(bar_plot_role)

report = dp.Report(
    dp.Select(
        blocks=[
            dp.Group(
                dp.Text("## Datos Originales"),
                table,
                data_table,
                label="Visión General"
            ),
            dp.Group(
                dp.Text("## Distribución por Género"),
                bar_plot_gender_dp,
                label="Análisis por Género"
            ),
            dp.Group(
                dp.Text("## Distribución por Facción"),
                pie_plot_faction_dp,
                label="Análisis por Facción"
            ),
            dp.Group(
                dp.Text("## Distribución por Rol"),
                bar_plot_role_dp,
                label="Análisis por Rol"
            )
        ]
    )
)

destination_path = os.path.join(base_path, "informe1.html")
report.save(path=destination_path, open=True)
