pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv/bin/activate'  // relative path from the workspace root
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Source the virtual environment and install dependencies
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    // Source the virtual environment and run the producer
                    sh '. venv/bin/activate && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    // Source the virtual environment and run the consumer
                    sh '. venv/bin/activate && spark-submit --master local[*] consumer.py'
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
