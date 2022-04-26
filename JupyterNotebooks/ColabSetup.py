#copy and paste into colab and run to generate an SSH host
'''
git_repo = 'https://github.com/<username>/<project name>'

!pip install colab_ssh --upgrade --quiet
from colab_ssh import launch_ssh_cloudflared, init_git_cloudflared
!pip install python-dotenv --quiet
import dotenv
import os
dotenv.load_dotenv(
        os.path.join('/content/drive/MyDrive/vscode-ssh', '.env')
    )
password = os.getenv('PASSWORD')
github_access_token = os.getenv('GITHUB_ACCESS_TOKEN')

# Install colab_ssh on google colab
!pip install colab_ssh --upgrade --quiet
from colab_ssh import launch_ssh_cloudflared, init_git_cloudflared

launch_ssh_cloudflared(password)
init_git_cloudflared(repository_url=git_repo + ".git",
         personal_token=github_access_token, 
         branch="main",
         email="<email>",
         username="<github username>")

#Password will be 'None' by default but can be changed above
'''