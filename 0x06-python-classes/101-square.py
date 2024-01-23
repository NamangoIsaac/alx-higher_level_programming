{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x06-python-classes":{"items":[{"name":"0-square.py","path":"0x06-python-classes/0-square.py","contentType":"file"},{"name":"1-square.py","path":"0x06-python-classes/1-square.py","contentType":"file"},{"name":"100-singly_linked_list.py","path":"0x06-python-classes/100-singly_linked_list.py","contentType":"file"},{"name":"101-square.py","path":"0x06-python-classes/101-square.py","contentType":"file"},{"name":"102-square.py","path":"0x06-python-classes/102-square.py","contentType":"file"},{"name":"103-magic_class.py","path":"0x06-python-classes/103-magic_class.py","contentType":"file"},{"name":"2-square.py","path":"0x06-python-classes/2-square.py","contentType":"file"},{"name":"3-square.py","path":"0x06-python-classes/3-square.py","contentType":"file"},{"name":"4-square.py","path":"0x06-python-classes/4-square.py","contentType":"file"},{"name":"5-square.py","path":"0x06-python-classes/5-square.py","contentType":"file"},{"name":"6-square.py","path":"0x06-python-classes/6-square.py","contentType":"file"},{"name":"README.md","path":"0x06-python-classes/README.md","contentType":"file"}],"totalCount":12},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0-run","path":"0-run","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":9}},"fileTreeProcessingTime":3.530889,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":738238355,"defaultBranch":"master","name":"alx-higher_level_programming","ownerLogin":"Louie-pixel","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2024-01-02T18:58:30.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/130101289?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1704222337.0","canEdit":false,"refType":"branch","currentOid":"17a0506a026cdf88870e3112e5a79f619bb39220"},"path":"0x06-python-classes/101-square.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","","\"\"\"Define a class Square.\"\"\"","","","class Square:","    \"\"\"Represent a square.\"\"\"","","    def __init__(self, size=0, position=(0, 0)):","        \"\"\"Initialize a new square.","","        Args:","            size (int): The size of the new square.","            position (int, int): The position of the new square.","        \"\"\"","        self.size = size","        self.position = position","","    @property","    def size(self):","        \"\"\"Get/set the current size of the square.\"\"\"","        return (self.__size)","","    @size.setter","    def size(self, value):","        if not isinstance(value, int):","            raise TypeError(\"size must be an integer\")","        elif value < 0:","            raise ValueError(\"size must be >= 0\")","        self.__size = value","","    @property","    def position(self):","        \"\"\"Get/set the current position of the square.\"\"\"","        return (self.__position)","","    @position.setter","    def position(self, value):","        if (not isinstance(value, tuple) or","                len(value) != 2 or","                not all(isinstance(num, int) for num in value) or","                not all(num >= 0 for num in value)):","            raise TypeError(\"position must be a tuple of 2 positive integers\")","        self.__position = value","","    def area(self):","        \"\"\"Return the current area of the square.\"\"\"","        return (self.__size * self.__size)","","    def my_print(self):","        \"\"\"Print the square with the # character.\"\"\"","        if self.__size == 0:","            print(\"\")","            return","","        [print(\"\") for i in range(0, self.__position[1])]","        for i in range(0, self.__size):","            [print(\" \", end=\"\") for j in range(0, self.__position[0])]","            [print(\"#\", end=\"\") for k in range(0, self.__size)]","            print(\"\")","","    def __str__(self):","        \"\"\"Define the print() representation of a Square.\"\"\"","        if self.__size != 0:","            [print(\"\") for i in range(0, self.__position[1])]","        for i in range(0, self.__size):","            [print(\" \", end=\"\") for j in range(0, self.__position[0])]","            [print(\"#\", end=\"\") for k in range(0, self.__size)]","            if i != self.__size - 1:","                print(\"\")","        return (\"\")"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[],[{"start":0,"end":28,"cssClass":"pl-s"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":12,"cssClass":"pl-v"}],[{"start":4,"end":29,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":31,"end":39,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":8,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":51,"cssClass":"pl-s"}],[{"start":0,"end":64,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":32,"cssClass":"pl-s1"}],[],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":53,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":27,"cssClass":"pl-s1"}],[],[{"start":4,"end":16,"cssClass":"pl-en"},{"start":5,"end":9,"cssClass":"pl-s1"},{"start":10,"end":16,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-en"},{"start":26,"end":31,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":53,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":28,"cssClass":"pl-v"},{"start":29,"end":48,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-s1"}],[],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":57,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":31,"cssClass":"pl-s1"}],[],[{"start":4,"end":20,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":28,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":15,"cssClass":"pl-c1"},{"start":16,"end":26,"cssClass":"pl-en"},{"start":27,"end":32,"cssClass":"pl-s1"},{"start":34,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"}],[{"start":16,"end":19,"cssClass":"pl-en"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":34,"cssClass":"pl-c1"}],[{"start":16,"end":19,"cssClass":"pl-c1"},{"start":20,"end":23,"cssClass":"pl-en"},{"start":24,"end":34,"cssClass":"pl-en"},{"start":35,"end":38,"cssClass":"pl-s1"},{"start":40,"end":43,"cssClass":"pl-s1"},{"start":45,"end":48,"cssClass":"pl-k"},{"start":49,"end":52,"cssClass":"pl-s1"},{"start":53,"end":55,"cssClass":"pl-c1"},{"start":56,"end":61,"cssClass":"pl-s1"},{"start":63,"end":65,"cssClass":"pl-c1"}],[{"start":16,"end":19,"cssClass":"pl-c1"},{"start":20,"end":23,"cssClass":"pl-en"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":28,"end":30,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-k"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":49,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":77,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":31,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":52,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":52,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":20,"cssClass":"pl-s"}],[{"start":12,"end":18,"cssClass":"pl-k"}],[],[{"start":9,"end":14,"cssClass":"pl-en"},{"start":15,"end":17,"cssClass":"pl-s"},{"start":19,"end":22,"cssClass":"pl-k"},{"start":23,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":33,"cssClass":"pl-en"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":37,"end":41,"cssClass":"pl-s1"},{"start":42,"end":52,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-s1"}],[{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":30,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-k"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":41,"end":46,"cssClass":"pl-en"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":50,"end":54,"cssClass":"pl-s1"},{"start":55,"end":65,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"}],[{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":30,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-k"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":41,"end":46,"cssClass":"pl-en"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":50,"end":54,"cssClass":"pl-s1"},{"start":55,"end":61,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":20,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"}],[{"start":8,"end":60,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":21,"cssClass":"pl-s"},{"start":23,"end":26,"cssClass":"pl-k"},{"start":27,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":32,"end":37,"cssClass":"pl-en"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-s1"},{"start":46,"end":56,"cssClass":"pl-s1"},{"start":57,"end":58,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-s1"}],[{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":30,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-k"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":41,"end":46,"cssClass":"pl-en"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":50,"end":54,"cssClass":"pl-s1"},{"start":55,"end":65,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"}],[{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":30,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-k"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":41,"end":46,"cssClass":"pl-en"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":50,"end":54,"cssClass":"pl-s1"},{"start":55,"end":61,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":24,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":18,"cssClass":"pl-s"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Louie-pixel/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Louie-pixel/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/Louie-pixel/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"101-square.py","displayUrl":"https://github.com/Louie-pixel/alx-higher_level_programming/blob/master/0x06-python-classes/101-square.py?raw=true","headerInfo":{"blobSize":"2.14 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"9eeaa5c","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FLouie-pixel%2Falx-higher_level_programming%2Fblob%2Fmaster%2F0x06-python-classes%2F101-square.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"71","truncatedSloc":"58"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Louie-pixel/alx-higher_level_programming/discussions/new","newIssuePath":"/Louie-pixel/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Louie-pixel/alx-higher_level_programming/blob/master/0x06-python-classes/101-square.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/Louie-pixel/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/Louie-pixel/alx-higher_level_programming/raw/master/0x06-python-classes/101-square.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Louie-pixel","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"Square","kind":"class","ident_start":57,"ident_end":63,"extent_start":51,"extent_end":2188,"fully_qualified_name":"Square","ident_utf16":{"start":{"line_number":5,"utf16_col":6},"end":{"line_number":5,"utf16_col":12}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":70,"utf16_col":19}}},{"name":"__init__","kind":"function","ident_start":104,"ident_end":112,"extent_start":100,"extent_end":382,"fully_qualified_name":"Square.__init__","ident_utf16":{"start":{"line_number":8,"utf16_col":8},"end":{"line_number":8,"utf16_col":16}},"extent_utf16":{"start":{"line_number":8,"utf16_col":4},"end":{"line_number":16,"utf16_col":32}}},{"name":"size","kind":"function","ident_start":406,"ident_end":410,"extent_start":402,"extent_end":500,"fully_qualified_name":"Square.size","ident_utf16":{"start":{"line_number":19,"utf16_col":8},"end":{"line_number":19,"utf16_col":12}},"extent_utf16":{"start":{"line_number":19,"utf16_col":4},"end":{"line_number":21,"utf16_col":28}}},{"name":"size","kind":"function","ident_start":527,"ident_end":531,"extent_start":523,"extent_end":741,"fully_qualified_name":"Square.size","ident_utf16":{"start":{"line_number":24,"utf16_col":8},"end":{"line_number":24,"utf16_col":12}},"extent_utf16":{"start":{"line_number":24,"utf16_col":4},"end":{"line_number":29,"utf16_col":27}}},{"name":"position","kind":"function","ident_start":765,"ident_end":773,"extent_start":761,"extent_end":871,"fully_qualified_name":"Square.position","ident_utf16":{"start":{"line_number":32,"utf16_col":8},"end":{"line_number":32,"utf16_col":16}},"extent_utf16":{"start":{"line_number":32,"utf16_col":4},"end":{"line_number":34,"utf16_col":32}}},{"name":"position","kind":"function","ident_start":902,"ident_end":910,"extent_start":898,"extent_end":1233,"fully_qualified_name":"Square.position","ident_utf16":{"start":{"line_number":37,"utf16_col":8},"end":{"line_number":37,"utf16_col":16}},"extent_utf16":{"start":{"line_number":37,"utf16_col":4},"end":{"line_number":43,"utf16_col":31}}},{"name":"area","kind":"function","ident_start":1243,"ident_end":1247,"extent_start":1239,"extent_end":1350,"fully_qualified_name":"Square.area","ident_utf16":{"start":{"line_number":45,"utf16_col":8},"end":{"line_number":45,"utf16_col":12}},"extent_utf16":{"start":{"line_number":45,"utf16_col":4},"end":{"line_number":47,"utf16_col":42}}},{"name":"my_print","kind":"function","ident_start":1360,"ident_end":1368,"extent_start":1356,"extent_end":1754,"fully_qualified_name":"Square.my_print","ident_utf16":{"start":{"line_number":49,"utf16_col":8},"end":{"line_number":49,"utf16_col":16}},"extent_utf16":{"start":{"line_number":49,"utf16_col":4},"end":{"line_number":59,"utf16_col":21}}},{"name":"__str__","kind":"function","ident_start":1764,"ident_end":1771,"extent_start":1760,"extent_end":2188,"fully_qualified_name":"Square.__str__","ident_utf16":{"start":{"line_number":61,"utf16_col":8},"end":{"line_number":61,"utf16_col":15}},"extent_utf16":{"start":{"line_number":61,"utf16_col":4},"end":{"line_number":70,"utf16_col":19}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Louie-pixel/alx-higher_level_programming/branches":{"post":"-w6qLdvpOZe4RtDsvXGUMpJSc3ioIlE3lg1jx_wudZDVUlo_gsaMDl6R2_E98Wl0lJnOlEoj6miq4IK9LRWehQ"},"/repos/preferences":{"post":"yalSdodcjiKDN8LHzad3_U_tIbDB3KJajqxj5tKscflyx4OZ_Udh1ATdHqyIeb_gBf8qHHY2F6SoYiYLUST0ZA"}}},"title":"alx-higher_level_programming/0x06-python-classes/101-square.py at master · Louie-pixel/alx-higher_level_programming"}