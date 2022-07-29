"""Build static HTML site from directory of HTML templates and plain files."""
import shutil
import click
from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
# accept arguments and options
@click.command()
@click.option('-v', '--verbose', is_flag = True, help='list all operations')
@click.argument('directory')
def main(directory, verbose):
    """Top level command line interface."""

    # turn input directory into a path
    if verbose:
        click.echo('more options!!')
    q = Path(directory)
    # click.echo(type(directory))
    # click.echo(type(q))

    # check if the directory exist
    try:
        if not q.exists():
            raise FileNotFoundError
    except FileNotFoundError as f:
        click.echo('Error: \'' + directory + '\' is not a directory')
    
    # create new folder, exit if already exist
    outputFolder = q/'html'
    if outputFolder.exists():
        raise click.ClickException("output directory already exists.")
    outputFolder.mkdir()

    # read corresponding templated file
    jsonConfig = q/'config.json'
    tempFolder = q/'templates'
    staticFolder = q/'static'
    click.echo(jsonConfig.exists())
    click.echo(tempFolder.exists())

    # if static exists, copy over
    if staticFolder.exists():
        shutil.copytree(staticFolder, outputFolder/'static')

    context = {}
    templateFile = ""
    url = ""
    with jsonConfig.open() as f:
        jData = json.load(f)
        context = jData[0]['context']
        templateFile = jData[0]['template']
        url = jData[0]['url']
    

    # render with jinja
    jinjaEnv = Environment(
    loader=  FileSystemLoader(tempFolder),
    autoescape=select_autoescape(['html', 'xml']),
    )

    # jinjaEnv = Environment(
    #     loader = PackageLoader(directory),
    #     autoescape=select_autoescape()
    # )

    template = jinjaEnv.get_template(templateFile)

    # click.echo(template.render(context))
   
    # output file save the new html
    p = outputFolder/templateFile
    p.write_text(template.render(context))
    

    # TODO handle jinja inheritance


    
    

    
if __name__ == "__main__":
    main()