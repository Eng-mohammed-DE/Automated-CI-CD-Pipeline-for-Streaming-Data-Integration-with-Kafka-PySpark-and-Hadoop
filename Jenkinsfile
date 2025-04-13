pipeline {
    agent any
    stages {
        stage('Set Up Virtualenv') {
            steps {
                script {
                    echo '🔧 Setting up virtual environment...'
                    sh '''
                        python3.11 -m venv /home/eng-mohammed/master_node/venv  # Create virtual environment
                        source /home/eng-mohammed/master_node/venv/bin/activate  # Activate virtual environment
                        pip install --upgrade pip  # Upgrade pip
                        pip install -r /home/eng-mohammed/master_node/requirements.txt  # Install dependencies
                    '''
                }
            }
        }
        stage('Check VENV Path') {
            steps {
                script {
                    echo '🔍 Verifying virtual environment setup...'
                    sh 'ls -la /home/eng-mohammed/master_node/venv'  # List the contents of the VENV
                }
            }
        }
    }
}
