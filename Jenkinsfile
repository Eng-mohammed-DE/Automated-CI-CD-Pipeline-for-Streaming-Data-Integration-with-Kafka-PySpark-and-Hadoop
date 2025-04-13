pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
    }

    stages {
        stage('Set Up Python Virtual Environment') {
            steps {
                script {
                    // Ensure Python is available, then create venv
                    sh 'python3 -m venv $VENV_PATH'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '. $VENV_PATH/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '. $VENV_PATH/bin/activate && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '. $VENV_PATH/bin/activate && spark-submit --master local[*] consumer.py'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo 'Cleaning up resources...'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline ran successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
