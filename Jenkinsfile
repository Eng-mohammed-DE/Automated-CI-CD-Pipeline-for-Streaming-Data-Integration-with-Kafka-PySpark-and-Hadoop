pipeline {
    agent any

    stages {
        stage('Prepare Virtual Environment') {
            steps {
                script {
                    sh '''
                        python3 --version
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi
                        . venv/bin/activate
                        pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
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
                echo 'Pipeline execution complete. Clean up if needed.'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ran successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
