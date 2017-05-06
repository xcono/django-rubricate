function DjangoStream(appElement, input)
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

DjangoStream.prototype.getModelFormElement = function()
{
    // get closest parent form element to stream app element
    var el = this.el;
    while ((el = el.parentElement) && el.tagName.toLocaleLowerCase() !== 'form') {}
    return el;
};

window.addEventListener('load', function () {
    [].forEach.call(document.getElementsByClassName('field-inkle'), function (el) {
        var app = document.createElement('div');
        el.classList.remove('hidden');
        el.appendChild(app);

        var input = document.getElementById('id_inkle');
        new DjangoStream(app, input);
    });
});
