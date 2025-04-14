pipeline {
    agent any
    stages {
        stage('Set Up Virtualenv') {
            steps {
                script {
                    try {
                        echo 'Setting up virtual environment...'

                        // Create the virtual environment if not exists
                        sh 'python3.11 -m venv /home/eng-mohammed/master_node/venv || echo "Virtual environment already exists"'

                        // Upgrade pip inside the virtual environment
                        sh '. /home/eng-mohammed/master_node/venv/bin/activate && pip install --upgrade pip'

                        // Install dependencies from requirements.txt
                        sh 'if [ -f /home/eng-mohammed/master_node/requirements.txt ]; then . /home/eng-mohammed/master_node/venv/bin/activate && pip install -r /home/eng-mohammed/master_node/requirements.txt; else echo "requirements.txt not found."; fi'

                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
        stage('Run Producer') {
            steps {
                script {
                    try {
                        echo 'Running producer.py...'
                        // Activate the virtual environment and run producer.py
                        sh '. /home/eng-mohammed/master_node/venv/bin/activate && python /home/eng-mohammed/master_node/producer.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
        stage('Run Consumer') {
            steps {
                script {
                    try {
                        echo 'Running consumer.py...'
                        // Activate the virtual environment and run consumer.py
                        sh '. /home/eng-mohammed/master_node/venv/bin/activate && python /home/eng-mohammed/master_node/consumer.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }
}
