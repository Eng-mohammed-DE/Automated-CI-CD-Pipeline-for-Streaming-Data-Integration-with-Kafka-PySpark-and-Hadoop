pipeline {
    agent any

    environment {
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Check if venv Exists') {
            steps {
                script {
                    sh '''
                        if [ -d "venv" ]; then
                            echo "❌ venv directory already exists. Exiting pipeline..."
                            exit 1
                        else
                            echo "✅ No existing venv. Proceeding with pipeline..."
                        fi
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        python producer.py
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        spark-submit --master local[*] consumer.py
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo '🧹 Cleaning up resources...'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ran successfully.'
        }
        failure {
            echo '❌ Pipeline failed or exited early.'
        }
    }
}
