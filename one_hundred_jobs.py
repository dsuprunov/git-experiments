from jinja2 import Template


if __name__ == '__main__':

    content = """
{% set cities = [
    "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Dresden",
    "Leipzig", "Nuremberg", "Hanover", "Bremen", "Kiel", "Magdeburg", "Potsdam", "Mainz", "Saarbrücken",
    "Erfurt", "Wiesbaden", "Mannheim", "Augsburg", "Freiburg", "Regensburg", "Karlsruhe", "Rostock",
    "Heidelberg", "Kassel", "Münster", "Dortmund", "Essen", "Bochum", "Wuppertal", "Bonn", "Gelsenkirchen",
    "Aachen", "Lübeck", "Halle", "Braunschweig", "Koblenz", "Trier", "Jena", "Hildesheim", "Würzburg",
    "Ingolstadt", "Cottbus", "Flensburg", "Görlitz", "Zwickau", "Bayreuth", "Gießen", "Paderborn", 
    "Osnabrück", "Offenbach", "Reutlingen", "Ulm", "Ludwigshafen", "Oldenburg", "Leverkusen", "Solingen", 
    "Herne", "Mülheim", "Düren", "Ludwigsburg", "Villingen-Schwenningen", "Neuss", "Siegen", "Tübingen", 
    "Celle", "Delmenhorst", "Dessau", "Hof", "Passau", "Schwerin", "Weimar", "Lüneburg", "Worms", 
    "Aschaffenburg", "Kempten", "Fulda", "Frankenthal", "Göttingen", "Speyer", "Rosenheim", "Remscheid", 
    "Konstanz", "Bergisch Gladbach", "Erkelenz", "Hamm", "Salzgitter", "Emden", "Erlangen", "Gera", 
    "Gladbeck", "Neubrandenburg", "Vechta", "Herford", "Homburg", "Lingen", "Neumünster", "Straubing", 
    "Greifswald", "Freising", "Suhl", "Coburg"
] %}

name: One hundred jobs

on:
  workflow_dispatch:
    inputs:
    {% for i in range(1, 101) %}
      run_job_{{ '%03d' % i }}:
        description: 'Job {{ '%03d' % i }} in {{ cities[i - 1] }}'
        required: true
        default: true
        type: boolean
    {% endfor %}

jobs:
    {% for i in range(1, 101) %}
  job_{{ '%03d' % i }}:
    if: github.event.inputs.run_job_{{ '%03d' % i }}
    runs-on: ubuntu-latest
    steps:
      - name: Job {{ '%03d' % i }} Step 1
        run: echo "Job {{ '%03d' % i }} Step 1 in {{ cities[i - 1] }}"
    {% endfor %}
    """

    template = Template(content)
    print(template.render())
