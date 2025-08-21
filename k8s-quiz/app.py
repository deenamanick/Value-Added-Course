from flask import Flask, request, render_template, redirect, url_for, session, make_response
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os

# --- App setup ---
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-me-please")

# --- Paths (deterministic, no system fallbacks) ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
FONT_DIR = os.path.join(STATIC_DIR, "fonts")
BG_PATH = os.path.join(STATIC_DIR, "certificate_bg.png")

# Use your exact bundled font filenames
FONT_BOLD_PATH = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
FONT_REG_PATH  = os.path.join(FONT_DIR, "DejaVuSans.ttf")

def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    if not os.path.exists(path):
        raise RuntimeError(f"Font not found: {path}. Did you copy it into static/fonts/?")
    return ImageFont.truetype(path, size=size)

def fit_font(draw, text: str, font_path: str,
             max_width_px: int, max_pt: int = 140, min_pt: int = 60, step: int = 2):
    """
    Shrink-to-fit text into max_width_px, using the same TTF for consistent metrics
    across host and Docker.
    """
    text = text.strip()
    for pt in range(max_pt, min_pt - 1, -step):
        f = load_font(font_path, pt)
        # textlength is precise for width; textbbox also works
        if draw.textlength(text, font=f) <= max_width_px:
            return f
    return load_font(font_path, min_pt)

# ======== Quiz questions ========
QUESTIONS = [
    {"id": 1, "question": "What is the smallest deployable unit in Kubernetes?", "options": ["Pod", "Container", "Deployment", "ReplicaSet"], "answer": 0},
    {"id": 2, "question": "Kubernetes was originally developed by Google.", "options": ["True", "False"], "answer": 0},
    # {"id": 3, "question": "Which component is the Kubernetes master node's brain?", "options": ["Kubelet", "Kube-proxy", "API Server", "Scheduler"], "answer": 2},
    # {"id": 4, "question": "A Kubernetes Namespace is used to logically isolate resources.", "options": ["True", "False"], "answer": 0},
    # {"id": 5, "question": "Which command lists all pods in the default namespace?", "options": ["kubectl get pods", "kubectl get nodes", "kubectl describe pods", "kubectl get services"], "answer": 0},
    
    # # ==== SERVICES & NETWORKING ====
    # {"id": 6, "question": "The default Kubernetes Service type is NodePort.", "options": ["True", "False"], "answer": 1},
    # {"id": 7, "question": "Which Service type exposes a service within the cluster only?", "options": ["ClusterIP", "NodePort", "LoadBalancer", "ExternalName"], "answer": 0},
    # {"id": 8, "question": "A ClusterIP Service can be accessed from outside the cluster.", "options": ["True", "False"], "answer": 1},
    # {"id": 9, "question": "Which Service type exposes a service on a static port on each Node’s IP?", "options": ["ClusterIP", "NodePort", "LoadBalancer", "ExternalName"], "answer": 1},
    # {"id": 10, "question": "Kubernetes DNS resolves service names to IP addresses.", "options": ["True", "False"], "answer": 0},

    # # ==== STORAGE ====
    # {"id": 11, "question": "Which object is used to persist data beyond a pod's lifecycle?", "options": ["PersistentVolume", "ConfigMap", "Secret", "Deployment"], "answer": 0},
    # {"id": 12, "question": "A ConfigMap can store sensitive information securely.", "options": ["True", "False"], "answer": 1},
    # {"id": 13, "question": "Which object binds a PersistentVolume to a pod?", "options": ["PersistentVolumeClaim", "StorageClass", "VolumeMount", "Secret"], "answer": 0},
    # {"id": 14, "question": "A PersistentVolumeClaim requests storage resources from a PersistentVolume.", "options": ["True", "False"], "answer": 0},
    # {"id": 15, "question": "Which Storage type dynamically provisions volumes?", "options": ["Static PV", "StorageClass", "ConfigMap", "Secret"], "answer": 1},

    # # ==== DEPLOYMENTS & CONTROLLERS ====
    # {"id": 16, "question": "A Deployment ensures the desired number of pod replicas.", "options": ["True", "False"], "answer": 0},
    # {"id": 17, "question": "Which object provides stable network identity for pods?", "options": ["ReplicaSet", "StatefulSet", "Deployment", "DaemonSet"], "answer": 1},
    # {"id": 18, "question": "A DaemonSet runs one copy of a pod on every node.", "options": ["True", "False"], "answer": 0},
    # {"id": 19, "question": "Which object is best for databases requiring stable storage?", "options": ["StatefulSet", "Deployment", "ReplicaSet", "Job"], "answer": 0},
    # {"id": 20, "question": "Jobs in Kubernetes are used for long-running services.", "options": ["True", "False"], "answer": 1},

    # # ==== RBAC & SECURITY ====
    # {"id": 21, "question": "RBAC stands for Role-Based Access Control.", "options": ["True", "False"], "answer": 0},
    # {"id": 22, "question": "Which object stores sensitive data like passwords?", "options": ["ConfigMap", "Secret", "ServiceAccount", "Namespace"], "answer": 1},
    # {"id": 23, "question": "Kubernetes Secrets are always encrypted at rest by default.", "options": ["True", "False"], "answer": 1},
    # {"id": 24, "question": "ServiceAccounts are used by pods to authenticate to the API server.", "options": ["True", "False"], "answer": 0},
    # {"id": 25, "question": "A NetworkPolicy can restrict pod-to-pod communication.", "options": ["True", "False"], "answer": 0},

    # # ==== INGRESS & LOAD BALANCING ====
    # {"id": 26, "question": "An Ingress resource manages external access to services.", "options": ["True", "False"], "answer": 0},
    # {"id": 27, "question": "Which resource defines HTTP/HTTPS routing rules?", "options": ["Service", "Ingress", "ConfigMap", "Secret"], "answer": 1},
    # {"id": 28, "question": "Ingress controllers must be installed separately.", "options": ["True", "False"], "answer": 0},
    # {"id": 29, "question": "Which type of Service is often used with Ingress?", "options": ["ClusterIP", "NodePort", "LoadBalancer", "Headless"], "answer": 0},
    # {"id": 30, "question": "An Ingress can perform SSL termination.", "options": ["True", "False"], "answer": 0},

    # # ==== HELM ====
    # {"id": 31, "question": "Helm is the package manager for Kubernetes.", "options": ["True", "False"], "answer": 0},
    # {"id": 32, "question": "What is the default name for a Helm package?", "options": ["Chart", "Template", "Release", "Bundle"], "answer": 0},
    # {"id": 33, "question": "Helm charts can include default values in values.yaml.", "options": ["True", "False"], "answer": 0},
    # {"id": 34, "question": "Which Helm command installs a chart?", "options": ["helm install", "helm apply", "helm run", "helm create"], "answer": 0},
    # {"id": 35, "question": "Helm 3 requires Tiller for installation.", "options": ["True", "False"], "answer": 1},

    # # ==== kubectl COMMANDS ====
    # {"id": 36, "question": "kubectl describe pod <pod-name> shows pod details.", "options": ["True", "False"], "answer": 0},
    # {"id": 37, "question": "Which kubectl command deletes a deployment?", "options": ["kubectl delete deploy <name>", "kubectl remove deploy <name>", "kubectl rm <name>", "kubectl erase deploy <name>"], "answer": 0},
    # {"id": 38, "question": "kubectl get all shows all resources in the current namespace.", "options": ["True", "False"], "answer": 0},
    # {"id": 39, "question": "Which flag specifies a namespace in kubectl commands?", "options": ["--ns", "--namespace", "--n", "--ns-name"], "answer": 1},
    # {"id": 40, "question": "kubectl logs <pod> fetches logs from the first container in the pod.", "options": ["True", "False"], "answer": 0},

    # # ==== SCALING ====
    # {"id": 41, "question": "Which command scales a deployment to 5 replicas?", "options": ["kubectl scale deploy <name> --replicas=5", "kubectl set replicas=5", "kubectl resize <name> 5", "kubectl scale pods=5"], "answer": 0},
    # {"id": 42, "question": "Horizontal Pod Autoscaler adjusts replicas based on CPU/memory usage.", "options": ["True", "False"], "answer": 0},
    # {"id": 43, "question": "HPA can only scale pods horizontally, not vertically.", "options": ["True", "False"], "answer": 0},
    # {"id": 44, "question": "Cluster Autoscaler adds/removes worker nodes automatically.", "options": ["True", "False"], "answer": 0},
    # {"id": 45, "question": "kubectl autoscale is used to create an HPA resource.", "options": ["True", "False"], "answer": 0},

    # # ==== MONITORING ====
    # {"id": 46, "question": "Prometheus is commonly used to monitor Kubernetes clusters.", "options": ["True", "False"], "answer": 0},
    # {"id": 47, "question": "Grafana can visualize metrics collected from Kubernetes.", "options": ["True", "False"], "answer": 0},
    # {"id": 48, "question": "kubectl top shows resource usage metrics.", "options": ["True", "False"], "answer": 0},
    # {"id": 49, "question": "Metrics Server must be installed to use kubectl top.", "options": ["True", "False"], "answer": 0},
    # {"id": 50, "question": "Fluentd is a Kubernetes-native monitoring tool.", "options": ["True", "False"], "answer": 1},

    # # ==== ADVANCED ====
    # {"id": 51, "question": "A Custom Resource Definition allows you to create new Kubernetes resource types.", "options": ["True", "False"], "answer": 0},
    # {"id": 52, "question": "Operators automate the management of Kubernetes applications.", "options": ["True", "False"], "answer": 0},
    # {"id": 53, "question": "etcd is used as Kubernetes’ key-value store.", "options": ["True", "False"], "answer": 0},
    # {"id": 54, "question": "etcd stores Kubernetes events permanently.", "options": ["True", "False"], "answer": 1},
    # {"id": 55, "question": "The API Server communicates with etcd to store cluster state.", "options": ["True", "False"], "answer": 0},

    # # ==== (continue in same pattern until id=100) ====
    #     # ==== SCHEDULING ====
    # {"id": 56, "question": "A Kubernetes scheduler assigns pods to nodes based on resource requirements.", "options": ["True", "False"], "answer": 0},
    # {"id": 57, "question": "Which concept allows specifying where pods should run?", "options": ["Taints", "Tolerations", "NodeSelectors", "All of the above"], "answer": 3},
    # {"id": 58, "question": "Taints prevent pods from being scheduled unless they tolerate them.", "options": ["True", "False"], "answer": 0},
    # {"id": 59, "question": "Node Affinity rules decide which nodes a pod can run on.", "options": ["True", "False"], "answer": 0},
    # {"id": 60, "question": "Pod Priority and Preemption can evict lower-priority pods to schedule higher-priority ones.", "options": ["True", "False"], "answer": 0},

    # # ==== POD LIFECYCLE ====
    # {"id": 61, "question": "Init containers always run before app containers.", "options": ["True", "False"], "answer": 0},
    # {"id": 62, "question": "Which status means the pod is waiting to be scheduled?", "options": ["Running", "Pending", "CrashLoopBackOff", "Completed"], "answer": 1},
    # {"id": 63, "question": "A pod in CrashLoopBackOff is repeatedly failing and restarting.", "options": ["True", "False"], "answer": 0},
    # {"id": 64, "question": "A pod with restartPolicy=Never will restart automatically on failure.", "options": ["True", "False"], "answer": 1},
    # {"id": 65, "question": "Which field in a pod spec defines the container image to run?", "options": ["image", "containerName", "command", "run"], "answer": 0},

    # # ==== LOGGING & DEBUGGING ====
    # {"id": 66, "question": "kubectl exec can be used to run commands inside a running pod.", "options": ["True", "False"], "answer": 0},
    # {"id": 67, "question": "Which command streams logs from a pod in real time?", "options": ["kubectl logs -f", "kubectl tail", "kubectl stream", "kubectl watch logs"], "answer": 0},
    # {"id": 68, "question": "Ephemeral containers are used for debugging running pods.", "options": ["True", "False"], "answer": 0},
    # {"id": 69, "question": "kubectl port-forward allows accessing a pod locally on your machine.", "options": ["True", "False"], "answer": 0},
    # {"id": 70, "question": "Which command shows events for a specific namespace?", "options": ["kubectl get events --namespace=<name>", "kubectl describe ns <name>", "kubectl events ns <name>", "kubectl view events <name>"], "answer": 0},

    # # ==== UPGRADES & MAINTENANCE ====
    # {"id": 71, "question": "kubectl drain <node> safely evicts pods from a node before maintenance.", "options": ["True", "False"], "answer": 0},
    # {"id": 72, "question": "kubectl cordon <node> marks a node as unschedulable.", "options": ["True", "False"], "answer": 0},
    # {"id": 73, "question": "Which command uncordons a node?", "options": ["kubectl uncordon", "kubectl node uncordon", "kubectl enable node", "kubectl schedule node"], "answer": 0},
    # {"id": 74, "question": "Kubernetes supports zero-downtime upgrades for deployments.", "options": ["True", "False"], "answer": 0},
    # {"id": 75, "question": "RollingUpdate strategy replaces all pods at once.", "options": ["True", "False"], "answer": 1},

    # # ==== CLOUD INTEGRATION ====
    # {"id": 76, "question": "Kubernetes can run on AWS, Azure, and GCP.", "options": ["True", "False"], "answer": 0},
    # {"id": 77, "question": "EKS, AKS, and GKE are managed Kubernetes services.", "options": ["True", "False"], "answer": 0},
    # {"id": 78, "question": "Which AWS service provides a managed Kubernetes cluster?", "options": ["ECS", "EKS", "Fargate", "Lambda"], "answer": 1},
    # {"id": 79, "question": "GKE stands for Google Kubernetes Environment.", "options": ["True", "False"], "answer": 1},
    # {"id": 80, "question": "Azure AKS automatically handles control plane upgrades.", "options": ["True", "False"], "answer": 0},

    # # ==== SECURITY BEST PRACTICES ====
    # {"id": 81, "question": "Running containers as root is a security risk.", "options": ["True", "False"], "answer": 0},
    # {"id": 82, "question": "PodSecurityPolicies are enabled by default in Kubernetes 1.25+.", "options": ["True", "False"], "answer": 1},
    # {"id": 83, "question": "NetworkPolicies can be namespace-scoped.", "options": ["True", "False"], "answer": 0},
    # {"id": 84, "question": "Which of these is NOT a Kubernetes security resource?", "options": ["Secret", "RoleBinding", "ServiceAccount", "PersistentVolume"], "answer": 3},
    # {"id": 85, "question": "Enabling audit logs in Kubernetes helps track API requests.", "options": ["True", "False"], "answer": 0},

    # # ==== TROUBLESHOOTING ====
    # {"id": 86, "question": "kubectl describe is useful for debugging failing resources.", "options": ["True", "False"], "answer": 0},
    # {"id": 87, "question": "CrashLoopBackOff usually indicates a container is failing repeatedly.", "options": ["True", "False"], "answer": 0},
    # {"id": 88, "question": "If a pod is stuck in Pending, it might be due to insufficient resources.", "options": ["True", "False"], "answer": 0},
    # {"id": 89, "question": "kubectl delete pod will always stop the application permanently.", "options": ["True", "False"], "answer": 1},
    # {"id": 90, "question": "Which command force deletes a pod without waiting for grace period?", "options": ["kubectl delete pod <name> --grace-period=0 --force", "kubectl pod rm --now", "kubectl kill pod", "kubectl terminate pod"], "answer": 0},

    # # ==== MISCELLANEOUS ====
    # {"id": 91, "question": "Kube-proxy manages network rules for Kubernetes services.", "options": ["True", "False"], "answer": 0},
    # {"id": 92, "question": "Kubelet runs on every Kubernetes node.", "options": ["True", "False"], "answer": 0},
    # {"id": 93, "question": "Which Kubernetes version first introduced the Container Runtime Interface (CRI)?", "options": ["1.5", "1.6", "1.7", "1.8"], "answer": 1},
    # {"id": 94, "question": "The default namespace in Kubernetes is called 'kube-system'.", "options": ["True", "False"], "answer": 1},
    # {"id": 95, "question": "kubectl api-resources lists all resource types in the cluster.", "options": ["True", "False"], "answer": 0},

    # # ==== BACKUPS & RESTORES ====
    # {"id": 96, "question": "Velero is a popular tool for backing up Kubernetes clusters.", "options": ["True", "False"], "answer": 0},
    # {"id": 97, "question": "etcdctl is a CLI tool to interact with etcd directly.", "options": ["True", "False"], "answer": 0},
    # {"id": 98, "question": "Backups of etcd should be encrypted.", "options": ["True", "False"], "answer": 0},
    # {"id": 99, "question": "A restore from backup always requires the cluster to be restarted.", "options": ["True", "False"], "answer": 1},
    # {"id": 100, "question": "Disaster recovery planning is not necessary for Kubernetes clusters.", "options": ["True", "False"], "answer": 1}
   
]

# ======== Certificate rendering ========
def build_certificate_image(name: str, date_str: str) -> Image.Image:
    if not os.path.exists(BG_PATH):
        raise RuntimeError(f"Background not found: {BG_PATH}. Put your A4 landscape PNG there.")

    im = Image.open(BG_PATH).convert('RGBA')
    w, h = im.size
    draw = ImageDraw.Draw(im)

    # Normalize and fit name
    name = name.upper().strip()
    max_name_width = int(w * 0.72)   # allow 72% of page width for name
    font_name = fit_font(draw, name, FONT_BOLD_PATH, max_name_width, max_pt=100, min_pt=60, step=2)

    # Date can be fixed or also fit (fixed here)
    font_date = load_font(FONT_REG_PATH, 56)

    # Positions (tune once to match your artwork)
    name_x = w // 2
    name_y = int(h * 0.460)   # ~46% from top
    date_x = int(w * 0.130)   # ~13% from left
    date_y = int(h * 0.750)   # ~75% from top

    # Draw
    draw.text((name_x, name_y), name, fill=(0, 0, 0), font=font_name, anchor='mm')  # center
    draw.text((date_x, date_y), date_str, fill=(0, 0, 0), font=font_date, anchor='lm')  # left/middle

    return im

def _image_bytes(name: str, date_str: str) -> bytes:
    img = build_certificate_image(name, date_str)
    buf = BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()

# ======== Routes ========
@app.route("/", methods=["GET", "POST"])
def capture_name():
    if request.method == "POST":
        name = request.form.get("participant_name", "").strip()
        if not name:
            return render_template("name.html", error="Please enter your name.")
        session["participant_name"] = name
        return redirect(url_for("quiz"))
    return render_template("name.html")

@app.route("/quiz")
def quiz():
    if "participant_name" not in session:
        return redirect(url_for("capture_name"))
    return render_template("quiz.html", questions=QUESTIONS)

@app.route("/submit", methods=["POST"])
def submit():
    if "participant_name" not in session:
        return redirect(url_for("capture_name"))

    score = 0
    total = len(QUESTIONS)
    incorrect_answers = []

    for q in QUESTIONS:
        ans = request.form.get(f"q{q['id']}")
        if ans is not None and ans.isdigit():
            submitted = int(ans)
            if submitted == q['answer']:
                score += 1
            else:
                incorrect_answers.append({
                    "question": q['question'],
                    "correct": q['options'][q['answer']],
                    "yours": q['options'][submitted]
                })

    participant_name = session["participant_name"]
    today_str = datetime.today().strftime("%d.%m.%Y")

    return render_template(
        "results.html",
        name=participant_name,
        date_str=today_str,
        score=score,
        total=total,
        incorrect_answers=incorrect_answers
    )

@app.route("/certificate-image")
def certificate_image():
    """Return a PNG certificate (stable size)."""
    name = request.args.get("name", "STUDENT")
    date_str = request.args.get("date", datetime.today().strftime("%d.%m.%Y"))
    download = request.args.get("download")

    data = _image_bytes(name, date_str)
    resp = make_response(data)
    resp.mimetype = "image/png"
    if download:
        resp.headers["Content-Disposition"] = f'attachment; filename=\"certificate_{name}.png\"'
    return resp

@app.route("/certificate-pdf")
def certificate_pdf():
    """Return an A4 PDF by embedding the generated PNG."""
    name = request.args.get("name", "STUDENT")
    date_str = request.args.get("date", datetime.today().strftime("%d.%m.%Y"))

    img_data = _image_bytes(name, date_str)
    img = Image.open(BytesIO(img_data)).convert("RGB")

    buf = BytesIO()
    img.save(buf, format="PDF", resolution=300)
    pdf_bytes = buf.getvalue()

    resp = make_response(pdf_bytes)
    resp.mimetype = "application/pdf"
    resp.headers["Content-Disposition"] = f'attachment; filename=\"certificate_{name}.pdf\"'
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # use_reloader=False prevents duplicate PIDs on dev
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
