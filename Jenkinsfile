pipeline {
    agent any

    environment {
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Use dot (.) instead of 'source'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    // Use dot (.) instead of 'source'
                    sh '. venv/bin/activate && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    // Use dot (.) instead of 'source'
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
