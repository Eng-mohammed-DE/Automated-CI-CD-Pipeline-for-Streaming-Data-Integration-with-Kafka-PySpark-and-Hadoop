pipeline {
    agent any
    stages {
        stage('Set Up Virtualenv') {
            steps {
                script {
                    echo 'Setting up virtual environment...'
                    sh 'python3.11 -m venv /home/eng-mohammed/master_node/venv'
                    sh 'source /home/eng-mohammed/master_node/venv/bin/activate && pip install --upgrade pip'
                    sh 'source /home/eng-mohammed/master_node/venv/bin/activate && pip install -r /home/eng-mohammed/master_node/requirements.txt'
                }
            }
        }
        stage('Run Producer') {
            steps {
                script {
                    echo 'Running producer.py...'
                    sh 'source /home/eng-mohammed/master_node/venv/bin/activate && python /home/eng-mohammed/master_node/producer.py'
                }
            }
        }
        stage('Run Consumer') {
            steps {
                script {
                    echo 'Running consumer.py...'
                    sh 'source /home/eng-mohammed/master_node/venv/bin/activate && python /home/eng-mohammed/master_node/consumer.py'
                }
            }
        }
        stage('Check VENV Path') {
            steps {
                script {
                    echo 'Checking VENV Path...'
                    sh 'ls -la /home/eng-mohammed/master_node/venv'
                }
            }
        }
    }
}
