# This script formats any code segments in .rst files with black.

# The reason why we use this shell script is that CMD and Powershell do not
# evaluate the wildcard character * in advance and pass valid paths to
# blacken-docs. Therefore, we stick to this process until there is an update.

blacken-docs --py36-plus --line-length 79 */*rst
read -p "Press enter to close the window and continue."
