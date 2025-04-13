pipeline {
    agent any
    stages {
        stage('Set Up Virtualenv') {
            steps {
                script {
                    echo '🔧 Setting up virtual environment...'
                    sh '''
                        echo "Creating virtual environment..."
                        python3.11 -m venv /home/eng-mohammed/master_node/venv
                        if [ $? -ne 0 ]; then
                            echo "❌ Failed to create virtual environment!"
                            exit 1
                        fi
                        echo "Activating virtual environment..."
                        source /home/eng-mohammed/master_node/venv/bin/activate
                        if [ $? -ne 0 ]; then
                            echo "❌ Failed to activate virtual environment!"
                            exit 1
                        fi
                        echo "Upgrading pip..."
                        pip install --upgrade pip
                        if [ $? -ne 0 ]; then
                            echo "❌ Failed to upgrade pip!"
                            exit 1
                        fi
                        echo "Installing dependencies..."
                        pip install -r /home/eng-mohammed/master_node/requirements.txt
                        if [ $? -ne 0 ]; then
                            echo "❌ Failed to install dependencies!"
                            exit 1
                        fi
                    '''
                }
            }
        }
        stage('Check VENV Path') {
            steps {
                script {
                    echo '🔍 Verifying virtual environment setup...'
                    sh 'ls -la /home/eng-mohammed/master_node/venv'  // List the contents of the VENV
                }
            }
        }
    }
}
