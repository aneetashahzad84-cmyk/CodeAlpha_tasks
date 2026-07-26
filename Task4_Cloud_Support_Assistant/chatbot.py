from tkinter import *

root = Tk()
root.title("Cloud Support Assistant")
root.geometry("700x600")
root.configure(bg="lightblue")

Label(root, text="Cloud Support Assistant", font=("Arial", 20, "bold"), bg="lightblue").pack(pady=10)
Label(root, text="Ask questions about Cloud Computing", font=("Arial", 12), bg="lightblue").pack()

chat = Text(root, width=70, height=20, font=("Arial", 11))
chat.pack(pady=10)

chat.insert(END, "Bot: Welcome! Ask me any Cloud Computing question.\n\n")

entry = Entry(root, width=55, font=("Arial", 12))
entry.pack(pady=10)

responses = {
    "cloud computing": "Cloud computing provides services like servers, storage, databases and networking over the Internet.",
    "aws": "AWS (Amazon Web Services) is one of the most popular cloud computing platforms.",
    "azure": "Microsoft Azure is a cloud platform used to build and manage applications.",
    "google cloud": "Google Cloud Platform (GCP) offers cloud services such as storage, computing and AI.",
    "iaas": "IaaS provides virtual machines, storage and networking over the Internet.",
    "paas": "PaaS provides a platform for developing and deploying applications.",
    "saas": "SaaS allows users to access software through a web browser.",
    "cloud storage": "Cloud storage allows users to store and access data online.",
    "virtual machine": "A virtual machine is a software-based computer running on a physical server.",
    "security": "Cloud security protects cloud systems and data from unauthorized access."
}

def send():
    question = entry.get().strip()

    if question == "":
        return

    chat.insert(END, "You: " + question + "\n")

    answer = "Sorry, I can only answer basic cloud computing questions."

    question = question.lower()

    for key in responses:
        if key in question:
            answer = responses[key]
            break

    chat.insert(END, "Bot: " + answer + "\n\n")
    chat.see(END)
    entry.delete(0, END)

Button(root, text="Send", command=send, bg="green", fg="white", width=15).pack(pady=5)

Button(root, text="Clear Chat", command=lambda: chat.delete("1.0", END), bg="orange", width=15).pack(pady=5)

Button(root, text="Exit", command=root.destroy, bg="red", fg="white", width=15).pack(pady=5)

root.mainloop()