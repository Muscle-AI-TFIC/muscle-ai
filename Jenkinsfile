pipeline {
    agent {
        node {
            label 'Muscle-Agent'
        }
    }

    options {
        timeout(time: 1, unit: 'HOURS')
        retry(1)
    }

    environment {
        POETRY_HOME = "${WORKSPACE}/.poetry"
        PATH = "${POETRY_HOME}/bin:${PATH}"
    }

    stages {

        stage('Install Python & Poetry') {
            steps {
                echo "Install Python and Poetry"
                
                sh '''
                    apt-get update && apt-get install -y python3 python3-pip
                '''

                sh '''
                    curl -sSL https://install.python-poetry.org
                '''

            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies"
                sh '''
                poetry install --no-interaction --no-root
                '''
            }
            post {
                success{
                    echo "dependencies passed"
                }
                failure{
                    echo "dependencies failed"
                    sh 'tail -n 10 install_log.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests"
                sh '''
                poetry run pytest 
                '''
            }
            post {
                success {
                    echo "Tests passed"
                }
                failure {
                    echo "Tests failed."
                    sh 'tail -n 10 test_log.txt'
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building project"
                sh '''
                poetry build
                '''
            }
            post {
                success {
                    echo "Build completed"
                }
                failure{
                    echo "Build not completed"

                    sh 'tail -n 10 build_log.txt'
                }
            }
        }
    }   
}
