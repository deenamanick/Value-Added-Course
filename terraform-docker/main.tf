terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# resource "docker_image" "quiz_app" {
#   name = "quiz-app:${filesha256("${path.module}/../k8s-quiz/Dockerfile")}"
#   build {
#     context    = "/home/vagrant/terraform-docker/k8s-quiz"
#     dockerfile = "Dockerfile"
#   }
# }


resource "docker_image" "quiz_app" {
  name = "quiz-app:${filesha256("${path.module}/../k8s-quiz/Dockerfile")}"
  build {
    context    = "${path.module}/../k8s-quiz"
    dockerfile = "Dockerfile"
  }

  triggers = {
    app_code = filesha256("${path.module}/../k8s-quiz/app.py")
  }
  keep_locally = false
}


resource "docker_container" "quiz_app" {
  name  = "quiz_app"
  image = docker_image.quiz_app.image_id

  ports {
    internal = 5000
    external = 5000
  }

  lifecycle {
    replace_triggered_by = [docker_image.quiz_app]
  }
}