class Model {
    constructor() {
        this.topics = [{
                id: 1,
                text: 'Overview of GANs',
                complete: false
            },
            {
                id: 2,
                text: 'Deep Dive into ADAM Optimizer',
                complete: false
            },
            {
                id: 3,
                text: 'LSTMs Implementation',
                complete: false
            }
        ]
    }

    addTopic(topicText) {
        const newTopic = {
            id: this.topics.length > 0 ? this.topics[this.topics.length - 1].id + 1 : 1,
            text: topicText,
            complete: false
        }

        this.topics.push(newTopic)

        this.onTopicListChanged(this.topics)

    }

    editTopic(id, updatedText) {
        this.topics = this.topics.map((topic) => topic.id == id ? {
            id: topic.id,
            text: updatedText,
            complete: topic.complete
        } : topic)

        this.onTopicListChanged(this.topics)
    }

    deleteTopic(id) {
        this.topics = this.topics.filter((topic) => topic.id !== id)

        this.onTopicListChanged(this.topics)
    }

    toggleTopic(id) {
        this.topics = this.topics.map((topic) => topic.id === id ? {
            id: topic.id,
            text: topic.text,
            complete: !topic.complete
        } : topic)

        this.onTopicListChanged(this.topics)
    }

    bindTopicListChanged(callback) {
        this.onTopicListChanged = callback
    }
}


class View {
    constructor() {
        this.page = this.getElement("#root")
        this.app_name = this.createElement("h1")
        this.app_name.textContent = "AI Topics List"

        this.form = this.createElement("form")
        this.input = this.createElement("input")
        this.input.type = "text"
        this.input.placeholder = "Type topic text here"
        this.addButton = this.createElement("button")
        this.addButton.textContent = "Add"

        this.topic_list = this.createElement("ul", "topic-list")

        this.form.append(this.input, this.addButton)
        this.page.append(this.app_name, this.form, this.topic_list)

    }

    displayTopics(topics) {
        while (this.topic_list.firstChild) {
            this.topic_list.removeChild(this.topic_list.firstChild)
        }

        if (topics.length === 0) {
            const p = this.createElement("p")
            p.textContent = "No topics added yet."
            this.topic_list.append(p)
        } else {
            topics.forEach(topic => {
                const li = this.createElement("li")
                li.id = topic.id

                const checkbox = this.createElement("input")
                checkbox.type = "checkbox"
                checkbox.checked = topic.complete

                const span = this.createElement("span")
                span.contentEditable = true
                span.classList.add('editable')

                if (topic.complete) {
                    const strike = this.createElement("s")
                    strike.textContent = topic.text
                    span.append(strike)
                } else {
                    span.textContent = topic.text
                }

                const deleteButton = this.createElement("button", "delete")
                deleteButton.textContent = "Delete"
                li.append(checkbox, span, deleteButton)

                this.topic_list.append(li)
            })
        }
    }

    bindAddTopic(handler) {
        this.form.addEventListener("submit", event => {
            event.preventDefault()
            if (this._topicText) {
                handler(this._topicText)
                this._resetInput()
            }
        })
    }

    bindDeleteTopic(handler) {
        this.topic_list.addEventListener('click', event => {
            if (event.target.className === 'delete') {
                const id = parseInt(event.target.parentElement.id)
                handler(id)
            }
        })
    }

    bindToggleTopic(handler) {
        this.topic_list.addEventListener('change', event => {
            if (event.target.type === 'checkbox') {
                const id = parseInt(event.target.parentElement.id)
                handler(id)
            }
        })
    }

    get _topicText() {
        return this.input.value
    }

    _resetInput() {
        this.input.value = ""
    }

    createElement(tag, className) {
        const element = document.createElement(tag)
        if (className) {
            element.classList.add(className)
        }
        return (element)
    }

    getElement(css_selector) {
        const element = document.querySelector(css_selector)
        return (element)
    }
}


class Controller {
    constructor(model, view) {
        this.model = model;
        this.view = view;
        // this.view.displayTopics(this.model.topics);

        //initial topics
        this.onTopicListChanged(this.model.topics)

        this.view.bindAddTopic(this.handleAddTopic)
        this.view.bindDeleteTopic(this.handleDeleteTopic)
        this.view.bindToggleTopic(this.handleToggleTopic)

        this.model.bindTopicListChanged(this.onTopicListChanged)

    }

    onTopicListChanged = (topics) => {
        this.view.displayTopics(topics)
    }

    // Controller has access to actually interact with the
    // model and in reaction to events.

    handleAddTopic = (topicText) => {
        this.model.addTopic(topicText)
    }

    handleEditTopic = (id, topicText) => {
        this.model.editTopic(id, topicText)
    }

    handleDeleteTopic = (id) => {
        this.model.deleteTopic(id)
    }

    handleToggleTopic = (id) => {
        this.model.toggleTopic(id)
    }
}

const app = new Controller(new Model(), new View())
