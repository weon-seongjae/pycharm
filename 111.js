if (app.documents.length == 0) {
    alert("문서가 열려있습니까?");
    exit();
}

if (app.selection.length > 0) {
    var myDoc = app.documents[0];
    var myTextFrames;
    var myNewTextFrame;
    var myOldTextFrame;
    var myGB;
    var myWidth;
    var myColumns;
    var myInterval;
    var i;
    var j;

    switch (app.selection[0].constructor.name) {
        case "Text":
        case "InsertionPoint":
        case "Character":
        case "Word":
        case "Line":
        case "Paragraph":
            myTextFrames = app.selection[0].parentTextFrames;
            break;
        case "TextFrame":
            myTextFrames = app.selection;
            break;
        default:
            alert("오류 \n 텍스트 프레임이 잡히지 않았습니다." + app.selection[0].constructor.name);
            exit();
    }

    for (i = 0; i < myTextFrames.length; i++) {
        myWidth = myTextFrames[i].textFramePreferences.textColumnFixedWidth;
        myColumns = myTextFrames[i].textFramePreferences.textColumnCount;
        myInterval = myWidth + myTextFrames[i].textFramePreferences.textColumnGutter;

        myTextFrames[i].textFramePreferences.textColumnCount = 1;
        myTextFrames[i].textFramePreferences.textColumnFixedWidth = myWidth;
        myTextFrames[i].textFramePreferences.useFixedColumnWidth = true;
        myTextFrames[i].textFramePreferences.useFixedColumnWidth = false;

        myOldTextFrame = myTextFrames[i];

        for (j = 1; j < myColumns; j++) {
            myNewTextFrame = myOldTextFrame.duplicate(undefined, [myInterval, 0]);
            myNewTextFrame.parentStory.texts[0].contents = "";
            myNewTextFrame.previousTextFrame = myOldTextFrame;
            myOldTextFrame = myNewTextFrame;
        }
    }
} else {
    alert("아무것도 선택하지 않았습니다! 텍스트 프레임을 선택하십시오.");
}