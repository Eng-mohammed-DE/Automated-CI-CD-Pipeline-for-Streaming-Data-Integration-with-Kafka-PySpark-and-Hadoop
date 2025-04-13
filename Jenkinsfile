pipeline {
    agent any

    environment {
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh 'source venv/bin/activate && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh 'source venv/bin/activate && spark-submit --master local[*] consumer.py'
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
