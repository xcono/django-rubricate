function DjangoRubricate(appElement, input)
{
    this.el = appElement;
    this.input = input;

    this.options = {
        defaultData: input.value.length > 2 ? JSON.parse(JSON.parse(input.value)) : {}, // escaped json parsed twice
        uploadUrl: function () {return '/rubricate/uploads/add'},
        csrfToken: function () {return ''},
    };

    this.app = Rubricate(this.el, this.options);

    this.getModelFormElement().onsubmit = function(){
        this.input.value = JSON.stringify(this.app.getData());
    }.bind(this);
}

DjangoRubricate.prototype.getModelFormElement = function()
{
    // get closest parent form element to stream app element
    var el = this.el;
    while ((el = el.parentElement) && el.tagName.toLocaleLowerCase() !== 'form') {}
    return el;
};

window.addEventListener('load', function () {
    [].forEach.call(document.getElementsByClassName('rubricate-input'), function (input) {

        var app = document.createElement('div');
        var form_row = input.parentNode.parentNode;
        form_row.classList.remove('hidden');
        form_row.appendChild(app);

        new DjangoRubricate(app, input);
    });
});
