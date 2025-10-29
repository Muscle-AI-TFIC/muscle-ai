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
                    sudo apt install python3
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
                }
            }
        }
    }   
}
