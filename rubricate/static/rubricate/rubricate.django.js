function DjangoRubricate(appElement, input)
{
    this.el = appElement;
    this.input = input;

    this.options = {
        defaultData: input.value.length > 2 ? JSON.parse(input.value) : {},
        uploadUrl: function () {return input.getAttribute('data-upload-url')},
        csrfToken: function () {return ''},
    };

    this.app = Rubricate(this.el, this.options);

    var _self = this;
    var updateInput = function(){
        _self.input.value = JSON.stringify(_self.app.getData());
    };

    setInterval(updateInput, 3000)
    this.getModelFormElement().addEventListener('submit', updateInput);
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
