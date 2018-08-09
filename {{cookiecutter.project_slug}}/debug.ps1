# Set python path
$env:PYTHONPATH = "."

# Get path of file
$file = $args[0]

# Execute python with ipdb debugger
python -m ipdb -c continue $file
