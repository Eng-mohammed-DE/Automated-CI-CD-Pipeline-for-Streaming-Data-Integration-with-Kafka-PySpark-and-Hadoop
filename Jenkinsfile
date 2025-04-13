pipeline {
    agent any

    environment {
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate full virtual environment path and install dependencies
                    sh '. $PYTHON_ENV && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    // Activate full virtual environment path and run producer
                    sh '. $PYTHON_ENV && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    // Activate full virtual environment path and run Spark consumer
                    sh '. $PYTHON_ENV && spark-submit --master local[*] consumer.py'
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
