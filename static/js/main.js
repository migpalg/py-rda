(function () {
    const processes = [
        {
            id: 1,
            title: "Process A",
            description: "Automated Process",
        },
        {
            id: 2,
            title: "Process B",
            description: "Automated Process",
        },
        {
            id: 3,
            title: "Process C",
            description: "Automated Process",
        },
    ];

    function createProcessCard({ title, description }) {
        const card = document.createElement("div");
        const cardBody = document.createElement("div");
        const cardTitle = document.createElement("h2");
        const cardDescription = document.createElement("p");
        const buttonWrapper = document.createElement("div");
        const button = document.createElement("button");

        card.classList.add("card");
        cardBody.classList.add("card-body");
        cardTitle.classList.add("card-title");
        cardDescription.classList.add("card-text");
        buttonWrapper.classList.add("d-grid", "gap-2");
        button.classList.add("btn", "btn-primary", "btn-block");

        cardTitle.innerText = title;
        cardDescription.innerText = description;
        button.innerText = "Execute";

        buttonWrapper.appendChild(button);
        cardBody.appendChild(cardTitle);
        cardBody.appendChild(cardDescription);
        cardBody.appendChild(buttonWrapper);
        card.append(cardBody);

        button.onclick = createProcessExecution({ title });

        return card;
    }

    function createProcessExecution({ title }) {
        return function () {
            Swal.fire({
                title: `Queued execution of "${title}"`,
                text: "Please wait until execution ends",
                icon: "info",
                confirmButtonText: "Cool!",
            });
            execute();
        };
    }

    function execute() {
        return fetch("/execute", {
            method: "POST",
            headers: new Headers({
                "Content-Type": "application/json",
            }),
        })
            .then((res) => res.blob())
            .then((blob) => {
                const file = window.URL.createObjectURL(blob);
                window.location.assign(file);
            });
    }

    function main() {
        const cardsOutlet = document.getElementById("cards-outlet");

        for (const process of processes) {
            const card = createProcessCard({ ...process });
            cardsOutlet.appendChild(card);
        }
    }

    document.addEventListener("DOMContentLoaded", main);
})();
