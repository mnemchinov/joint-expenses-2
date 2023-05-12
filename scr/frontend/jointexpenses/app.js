Ext.application({
    extend: 'JointExpenses.Application',

    name: 'JointExpenses',

    requires: [
        'JointExpenses.*'
    ],

    mainView: 'JointExpenses.view.main.Main'
});
