## Exercise: Isolated Environments with Dev Containers

**Duration:** 20-30 minutes
**Goal:** In this exercise, you will set up a Development Container in VS Code to create an isolated and reproducible development environment.

Responsible AI coding also means ensuring your development environment is reproducible and isolated. Dev Containers allow you to define a complete, containerized development environment in code, ensuring that all team members (and Copilot) are working with the exact same tools and dependencies.

>**Note**: This exercise assumes you have Docker installed and running on your machine. If you don't have Docker, please install it from [https://www.docker.com/get-started](https://www.docker.com/get-started) before proceeding.

***

### Step 1: Install the Dev Containers Extension

1. Open the Extensions view in VS Code (`Cmd+Shift+X` on Mac / `Ctrl+Shift+X` on Windows).
2. Search for **"Dev Containers"** (published by Microsoft).
3. Click **Install**.

***

### Step 2: Reopen Folder in a Container

1. On the left sidebar, click the 'Remote Explorer' icon (it looks like a computer with a remote connection) and expand the Dev Containers section.
2. Click 'reopen the current folder in a container'. This will trigger the command palette. (Alternatively, you can also open the command palette directly with `Cmd+Shift+P` / `Ctrl+Shift+P` and search for the command 'Dev Container: Reopen in Container').
3. Click 'Add configuration to workspace' when prompted. This will create a `.devcontainer` folder in your workspace with a `devcontainer.json` file inside it.
4. Choose an existing template configuration from the list, such as **Anaconda (Python 3)**. This will set up a pre-configured environment based on your selection.
5. VS Code will now reload the window and start building the Docker container based on your selection. This may take a few minutes the first time it downloads the image.

***

### Step 3: Inspect the Dev Container Configuration

1. Once the container is running and the workspace is fully loaded, notice the blue >< icon in the bottom-left corner of VS Code. This indicates you are connected to the Dev Container.
2. Look at your file explorer tree; you will see a new folder named `.devcontainer` was automatically added.
3. Open the `devcontainer.json` file inside it.
4. Inspect the file. This file acts as the blueprint for your environment, controlling how the container is built, which Docker image is used, which VS Code extensions are pre-installed in the container, and what scripts run after the container starts.

***

### Step 4: Verify the Remote Environment

1. Open a new terminal in VS Code (`Terminal -> New Terminal`). 
2. Because you are now inside the Dev Container, the terminal session is running inside the isolated Docker environment, not on your local machine.
3. Run a quick check to verify the environment. For example, if you chose the Python container, type:
   ```bash
   python --version
   ```
4. Check the OS distribution to prove you are in a container:
   ```bash
   cat /etc/os-release
   ```
5. Try installing a package (e.g., `pip install requests` or `apt-get install tree`). Notice how these changes are safely isolated to the container and do not pollute your local system!

***

### Step 5: Returning to Local Environment

1. If you want to close the container and return to your local environment, click the Dev Container icon in the bottom-left corner.
2. Select **`Reopen Folder Locally`** (or **`Close Remote Connection`**).
