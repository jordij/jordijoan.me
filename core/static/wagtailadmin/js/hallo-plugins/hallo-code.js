(function($) {
    return $.widget("IKS.hallocode", {
        options: {
            uuid: '',
            editable: null
        },

        populateToolbar: function(toolbar) {
            var widget = this,
                button = $('<span class="hallocode ui-buttonset"></span>');

            button.hallobutton({
                uuid: widget.options.uuid,
                editable: widget.options.editable,
                label: 'Code',
                icon: 'icon-code',
                command: null
            });

            button.on('click', function(event) {
                var lastSelection = widget.options.editable.getSelection();
                var selectionParent = lastSelection.startContainer.parentNode;

                if (selectionParent.tagName === "CODE") {
                    $(selectionParent).contents().unwrap();
                    var myBtn = $(this).find("button");
                    if (myBtn) {
                        myBtn.removeClass("ui-state-active");
                    }
                } else {
                    var elem = "<code>" + lastSelection + "</code>";
                    var node = lastSelection.createContextualFragment(elem);
                    lastSelection.deleteContents();
                    lastSelection.insertNode(node);

                    return widget.options.editable.element.trigger('change');
                }
            });

            var lastPosition = 0;
            $(".input").on("keyup click", function(event) {
                var sel = widget.options.editable.getSelection();
                var selectionParent;
                if (cursorMoved(event, sel)) {
                    var myBtn = button.find("button");
                    selectionParent = sel.startContainer.parentNode;
                    if (myBtn) {
                        if (selectionParent.tagName === "CODE") {
                            myBtn.addClass("ui-state-active");
                        } else {
                            myBtn.removeClass("ui-state-active");
                        }
                    }
                }
            });

            function cursorMoved(event, range) {
                var newPosition = getPosition(event, range);
                if (lastPosition) {
                    if (lastPosition.left != newPosition.left || lastPosition.top != newPosition.top) {
                        lastPosition = newPosition;
                        return true;
                    }
                } else {
                    if (newPosition != lastPosition) {
                        lastPosition = newPosition;
                        return true;
                    }
                }
                return false;
            }

            function getPosition(event, selection) {
                var eventType, position;
                if (!event) {
                  return;
                }
                eventType = event.type;
                switch (eventType) {
                  case 'keyup':
                    return getCursorPosition(selection);
                  case 'click':
                    return position = {
                      top: event.pageY,
                      left: event.pageX
                    };
                }
            }

            function getCursorPosition(range) {
                var newRange, position, tmpSpan;
                tmpSpan = jQuery("<span/>");
                newRange = rangy.createRange();
                newRange.setStart(range.endContainer, range.endOffset);
                newRange.insertNode(tmpSpan.get(0));
                position = {
                  top: tmpSpan.offset().top,
                  left: tmpSpan.offset().left
                };
                tmpSpan.remove();
                return position;
            }

            return toolbar.append(button);
        }
    });
})(jQuery);
