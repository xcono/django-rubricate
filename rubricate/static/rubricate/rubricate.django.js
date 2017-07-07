function DjangoRubricate(appElement, input)
{
    this.el = appElement;
    this.input = input;

    var defaultData = input.value.length > 2 ? JSON.parse(input.value) : {};
    defaultData = typeof defaultData === 'string' ? JSON.parse(defaultData) : defaultData;  // escaped json parsed twice

    this.options = {
        defaultData: defaultData,
        uploadUrl: function () {return input.getAttribute('data-upload-url')},
        csrfToken: function () {return ''},
    };

    this.app = Rubricate(this.el, this.options);

    var _self = this;
    setInterval(function() {
        // cache input data to present it in case of validation errors
        _self.input.value = JSON.stringify(_self.app.getData());
    }, 3000)

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
