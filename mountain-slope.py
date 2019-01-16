# Program used for hiking, to calculate the slope of a mountain based
# on data given by a gps program

import click

@click.group ()
def main ():
    pass


# implementation for command line using click framework
@main.command ()
@click.argument ("x1")
@click.argument ("y1")
@click.argument ("x2")
@click.argument ("y2")
def c (x1, y1, x2, y2):
    # x1, x2 in kms and y1, y2 in metres
    """ Calculates the slope with parameters: x1, y1, x2, y2 """
    delta_x = abs (float (x1) - float (x2)) * 1000 #delta_x in metres
    delta_y = abs (float (y1) - float (y2)) #delta_y is already in metres
    m_percent = delta_y / delta_x * 100
    click.echo ("Slope: %.2f%%" % m_percent)


if __name__ == "__main__":
  main ();
