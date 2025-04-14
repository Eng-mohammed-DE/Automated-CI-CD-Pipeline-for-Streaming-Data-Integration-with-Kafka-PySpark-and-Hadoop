pipeline {
    agent any
    stages {
        stage('Set Up Virtualenv') {
            steps {
                script {
                    try {
                        echo 'Setting up virtual environment...'

                        // Use root user (without sudo) for package installation
                        sh 'apt update && apt install -y python3.11-venv python3-pip python3-setuptools python3-dev'

                        // Create the virtual environment
                        sh 'python3.11 -m venv /home/eng-mohammed/master_node/venv'

                        // Upgrade pip inside the virtual environment
                        sh '. /home/eng-mohammed/master_node/venv/bin/activate && pip install --upgrade pip'

                        // Install dependencies from the requirements.txt file
                        sh '. /home/eng-mohammed/master_node/venv/bin/activate && pip install -r /home/eng-mohammed/master_node/requirements.txt'

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
                        sh '. /home/eng-mohammed/master_node/venv/bin/activate && python /home/eng-mohammed/master_node/consumer.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
        stage('Check VENV Path') {
            steps {
                script {
                    try {
                        echo 'Checking VENV Path...'
                        sh 'ls -la /home/eng-mohammed/master_node/venv'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }
}
