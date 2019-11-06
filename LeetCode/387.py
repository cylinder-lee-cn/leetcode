"""
387. 字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        f = l
        for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']:
            if (s.count(c) == 1):
                tmp = s.index(c)
                if (tmp < f):
                    f = tmp
        if (f == l):
            return -1
        else:
            return f


s = Solution()
print(s.firstUniqChar('leetcode'))
print(s.firstUniqChar(
    'fmjiooebgjatqjttfftvobormhubvgxpiobekkxujgvaktcewbvkdnqwqmeeaogpcgaliilvimtsqtlfnhtvvipwsesosgluwtpearpvrrlpjgppqgegejsruiwbnppnlonpsetvfverxhmtihrfcbspupgmhrqniosmosamujoxqdepvjrcnhgqmkuhrlbrwmwtldfjnnkjnvpfonuvpewusqxstgxcfikmcwcgkipootlemscowhstxcaefreafjfxtuqcbdvasncmijmvdjlwcqopxnxdwqafwugelnuwledeajbkvjilvbjkarimpesekhmoixfapihomeswgirtovrgjgarjglnjmshirxphafbghvxuwpxggpbkewemvtrrmjxscdjlfvnfuepqkjffkkmdcstaktwlwawxcpxdgxsidxmcnhhlrtpmqfafucwxdieasfjgueridmakgcehmqtehwbkvahedxscsniwpdannvbpobtskdgmpfijknlunawajfcrgvigbkrlmuonuubmaluqfsjvsajjixbqjqrvwbhebumwsjvmqovawxjqbrumpdttswmqmutdvqvvtujmkbdauckvdcfknhsrwxxaucfqhabuinedmrocivwmhtwlkvfuqjmnouvkquijisidwqoekheegfvxxvdcngjxrjtlxfcgufmcjvtxrjuhipeoenouagigobxjfcpblvirfjvtfbhdmrjpqpvsxhijumbfjehswteajcmqhcdbstolecqlktajmtrhmjddnoawocbohrjqlgckhhhrkbcwgvpxolrlhwuvebsumijspknesmsspcvibsemoccjndalknqlxguvwvhbeujhavjpflwpuexgwwmbaqmlqdilwbaixemaokwsdppqjtgkdgixhkmmoixssvatqguvqjuctwfpvpjulmuuprkobuhkasxabjxvhltaejkuxoxopojcxxnasxcnqwnqsngktxdbhpuxacxgpgfxieeubcgkulklslskdwvimqvpatdvkukejojafuvqbrpqkcbwpohesnmvgpsdqoordplnhnoacwsabsvwjbcujvrrcimqcolvnwckgfbkuuvuqmfjohxrkamlnfrmaexcqeordnwwclgsxpibbgetfwntxpbocgeguaxavmnlkbpkvdamhqlsriuqhempogbsicviftokeiowlreddnlfxvblgpcxhtgovkijdbbtjavfihmwtldogomedftgdwlkkbjlwgogjplgfqimhevlhcntxqaukoqoqoowxkntlxxkbrihahqvsrmikphqvdfrgjarngpkaptrfmufovumglkcdcjeefsmndqnrjccpqwcaiuhifbptjftksxownppntulkdqujrapdfqfxhhqssxbjophmsusfrgarnxawkjwgeqhsdgvlggvvodgwfcvvgexwgrofdsiquvuscopwoewjlkndexhgripagmggvbfswngxlpgrjxwcmtcdbmrqsrhhgchkhxntaklapsshhrdljaghmstcspinnctbkuhuukevmfcwqjgcsqjhtxnnqrsxttisubvusprxurqwnpxxatdkifxbmrnirhxghmnuixbwppcigtwusjmrddqvowawffxntxqeauojlfrebmdwrkttsqsjpiebknsvgqwdrvgbkvebqnnpeorbpwlogqssfhorkbgkukkomvnaktvhtfwkbmeumuqridupxasqacshphkippegghkprknspngnckmatxiwfhnevkvkqjhtwvvqganrsdogtswdavjtuifwfwuwmjjgknwuaowbkpwoemsbvcvalvqfqlpteqjqsqpuhewrbxacurhbtwmuexpanjajomgbhhwpmswbonkndhwubjvixmcamivcegbaqjmwoigsrhffchxrhdcmdfjmnaitohcgfvaaohnmthqkakkrfmrhaslnbbhxkwrkxvuoknvollvfnxpeemtkgmctplllsknnfxwhetmjbnkosnvjtlpeojmniwtswvxopfpmeklmfeqmgovbscpwxdktstjcuwioowhvibkqaqxirbptkhbpbiegaqllgngvbkgjsxqmrrhbuglqcmoincrgppswdjjsqrejcohbrxpqofrhspwbsqlkrgotemlfllqewnnppkrvxgbrlsbrijatuphrifkqtiltillftkdhpjkwedxihhrrdanjhfiihivgxkbenxwgxgffnexiibgltthtjslaamoemjxtwbslgfkgxulwchwjwhwnpvugmswvwiflnbwwfojtbtbnwrteumskqgskvducfhklkvmgksjjlqbtlpluljtimvxvdabdbohewgkuxxedovvarbpifibqutbhepwhtnmvqfbhugqhijuvqhhbrqtjxojpkcapsvjarqbqpqgneefkjsdoqskdnqxgnxkkwewcprbpclggpxbolqsaamwqphdttqlbidsnuhltnbpclaacpsoxdxhgmfmxgukmxdgrxrnngblqxacvljvcrlvvejebvsacmkcnjbamhkibdhgajtijbqaoalrsjufdvswkbwejxgxeioosjkpnlhpipkecjrjjmrcipqbdxmqkflqurfjghwlnrqnqnjdrqjnwtpwtgedssivnltqtwpecgudvgenwsrjuodfiuohnqdfpoocvhicrxoqakcvfjqedxuulbkgcgghhlnqesdekdockldurnapthceeoigtuanhrqshxpmvlnkkrqkqhiktnovccaindinxqphgxmqborqbdphswaemrowwgttcsqapicjscjrwedegjrcrcqpgdljpqprkrxwvcjglwihfvlvstpmktqrxuweolnamqfxevupqfarwccunchfxcrtkdfasmwsrakcscducgbrakgrwndnawjfnakvenifrigaiqgnicdfenbegujmnxjormlclvnktrbjfpojdhworurfuqtsnwravocjrmdixkdvrpbkdhleaoiujaqwackjcooalserxlnegbjwpcahqdfifmxrpmkspuoqdaptamnobemgxpggkmqcpmctkkllvbubrgmhfgucnimkmogcgxikhbquaodetfxduclvtalriwxjopgedxpigsbtkxmmswhnvwlfvkitsvhfudisjbeeuqnchgnmswujerogjfvquntepjkukhpnqkmxaswecmwnqeejxiqawodxpboetaiudiwlutgudawkbndpqdtkprwwtetahvhjekuwmchmulsqqpuvuhvxqvoadqibmuvmubmhifiuoedgfppwssoxadspiaxhchavtuhqppbtqubohxujlxosqskjsrpscwrditgpknlklbnghoefgleiqspxqnasuhradhxnqjebovnpvuvdmasaptprdtcghfgcnxeckcnacidjacbdnfquvgtpkefamvcswtdgxqoxxiouixwnalesecliwobgcilxgmoiieinmhfxwtorfahtbhigpuorsxtttresmvbtkuklkhqgvgrgwgqhmlnidsjeasukmdkjqamadsloqfcndovuffevwpmldiarixmphklwcejpnmdgaxfflbewtaoieshhxiwnxkxvwfbsfdstekcboxoujuwtuabdswxlpbivqwdwhsrkpodkfqahiuuelkwpisrahngnxwpnmswdctpojduxkhikarojsldfqrbgugnveclifsqwkaruuvkwemrkirvckkbipvnxwshxhsnsxqgvrosrouqkrvxhukwdplhltkbsjtgbisntxdjixhjqvvrthiahfilrstlxcflfowfwodvgxpvovmdiseqdinsrmmuhtrmurmgwhwxcvufsjhfegpeibbscqgurewbxavalkvidcmxvaipiliwohufnhadxuvkweqdeohgknrvhtgrmapevthbcakjxduijmgxsmfthwlfqjrlpwfqvnjqreewkkwjpbguvdnnkxqjpdcgtmravecqklhcqjaokdacfmbokocawjqqgtdwgqdleesgrxeaarmsswifblabdsttbcebrldqqagimnrfkddstcdrfhdohwuvuccjlcsxwobrldhxqcedsabmhscokhcqxsiohijxgxvceiofbgxgvxkfgtnbtcvsbttamdgsikcbimxgpgfbvqpemsvxusgftnfhjduxmqgahqcualvocswraraqdnmifpnthjiwrjlnimvgfvpttwcubfiebththkemgfeximjcnpcuotukcdavqrfugviwrnqcowxtbjowmkiocndcvksnvdogbsvjdjdopubiecmrouiuduetnchshttlumjuennoirlximstlwropaxvcupnismuvirpfkutkserxsbelxlmhqvqtathoisxfrhcohcgfcumxcquvigolfvmcncgcueommsvpvhfbpecbehlkjtutoirvmeeupshsecriubkojdrfjwrdbjhoefpnmcxminughquitsudrrtsrggnrifwxuwkglrbamekflpadsdkhposlwkdqjijgfwejhafopoexdlqtpwjcmetpwnmptoabbqcwhgwlwmnnrgqudxbdauophihnoblrpkvfssfhsfewmcqgnvrjmotjajnldxrgxfwnqukbsjdlewaawqtfxckfcswrjcepskchjmechqilcbpsnafhjasutjcoarkfhqmkwsvrqkvpvngncnagkqnfvirtbueawgdxwglhvhaonrfjfxektcbbpgkxtscxiwonkipdgqjjcnenhxjmdwpassgdonlkuhwfiqbgutsqvrkkhdpmtuhrngnwcurkcbdwspbpobscnfjpnenrjvqnqjpbaxkpstnradwxetiadrxnktumphldmdulxppavxmgrvjwhxnronnmnweuntrehmuvicigcmxmfoklwhjworllwxvsjkaaumghbbvickieemjhbreglwilgexgnsrwqdlamefhecfnprgbrhncoswtuhrpjflgvrdrrustacgauersnavjggtdahngdkijkpwroxctglfmwmbbftvnldiftmbcnjgxhtlbnhophnbkslppccdtoafpmfgewjwpfweqokoasjjskqtekupvgmcjluldpuaclbhppsrwpvwtftfpqrtllrouqqkixruqrknwcgbiptiweenjrbvuogsqujjsgariqdwupvehbrxswtcjpuojosoewakcejqsxdbrejdlvbkalivartpclpcipltisekhoraxtbolmslhldofievwvuwgvdelpbvhwhjtdfmxvdaapufrkqdnnbsedqhemrjbwmfivnpiqwstwekurpxikoncotccpcqggiumxjngfkbpjjefncdpntirishglfafgtvpurxinpeeounumhfbvqtqixuxfdkxhvksbvnhpnvdpwdkaighkwgagqrwpcwlagbvighsumsuuvpxrtnautrbdpasamescodhakestmuwdlaknkunuqdsgcavaaeumnirrkwxuwdcwhimwubobgvehdamxfnqolqcextqpqximivndjvkltxwgjrjwvbhqbllqhefndppwaqevaiblbrjeulenhoqtnilfebhvqfhlwjbltsfigdvieweslfuoaadefjoxvxbtsqnvjdtkmnjljjshjfkjldtmrgrmegnxmnitccokcgfetwwtjqdfebcvkgjdlbkfmpbogqmpppslclhxtexjfkiixcwumsbicqbfoffbnaaqwrvrxcnfvnhdikxavpjvgopbajkitjwuxpruvcocmtmrnfmgaktoqbujfetfrbfgghtnfurhbespwvgwejhsrlqnfnpphkmgrxswxaxmwixplqvrreurxtsnbwwpnkufbbxwevpbshlimhifhfcutqskxncmmsfkxlsnsmcpvaxsbkavgdssotstrtqgsswgrgkutnhvpflwsruoonudwmhivplvqbihbrpkfapmqeodilvcxmpandesntrcorkhwocxcfckbwqsbccarauikphpifcunaevhtdujdxkqsdrxmnavattusisowpdtpikwjjqrthrgkncqkddbglkvsqqogaqcgmfcqftmvjrduwnwegagameuaodcnecivaodawvrjgbqrpqprwhfxprbuucbdurptffbafxixvrtrhfndkjedujmfhgthxwgbtdmsrijhpcgeatpidnfmkvnnjwisoifxbpeulreaudisxlnbrlxcceukckjuahtnhsbhdbjttmaswuwokmrulprnssmnotklhtudiqqamnqgvoeojxntwfmwqhcnafbjgstxdwshihheecgluuspdwnueqdlnuaohppndmfxxkvejwmdeeiijsnrpniaobitidjtrrccrmsqhehpqfhoqcsljxpvkdhqrvxcensoexopemvxbshacfgljvkhccovtftkvjtmdcriqnxtgiipedxjqxhbnwvsgutcmuxuuwlunpfcqbsmbnhvnwikeinwjrjmawevxjedqkqwounmwkuobrerphmkfmewrqebwnmvuhwnbjrsokigtithvtdobvtjjrgwgsujwfrqjrxnxnkdmmumovlkgnqnvrknkwcrrmxhflnmjucoutjidutgemccaqpgxuptlnsjohninpaxcqbluikkkabxqpxrareamxratgfbdeefgimeqscvqdfwfgjntgaavkdkfphxsvoscnkeqbcihewfadveqeckoocadsrjdbgmtwelmfsdxlvvjquuqtuiguvcganrvqmmmlartokohbiwhumwlrnaoeuhgakfbticdnponnkiafixkxgcqqutnuxjkkawxrcwqlrbljkdrancucchqxtjugwwlpxewldxugplntsndiqvkebxcxbklrrxioxwghbwxupmkjchwxhbxfjqpxwfrfqmshiwrxgeqhdmlgcbjveorwudpxsdolunasssudagaxblxpsceawtaoiibxfutsdjdavdcjrhgkljpwlercesvfxwvqqaitossibralpwtcqntctffsabimhhebrpmewogkwmjbmcwoaqkdmglbjbassbglbjipjoxpvltbheihlkfcehjwxcwhxvcebvemjcugeawviebualtgfipbkmrugtrgxuhbvrwaurtupkafbcmhfqolcpkahttjnojimfelgpkpmwwknjcowaospcjlceodrtdqiuhbjbsvhhkmfotbhrwrrovvphvoflvsaxwrurewqwncxchlaigfqdghwnwkxfwvuokmbvqkplwvenxbbaiiernihucfrsxjurtjxxekuowuehdvcabrvxkbkuqbcshgixqqvfdvppmpqpsolpmamheqahjvcnpvirscnptdrvcwwwmvuwpoxxexxtekbtxvuhqwopfvicfshulqnfkkaqjwibsxxlgpmblmalikfuxceresomwevkmterkmmxmkaxkedfesreiwufciqttniffastvbankgjjwhqtlgtjhpoplmrrieiqdnbxlhtwadnwwenwdfsnntejhnkxwrmmpilulfnsvcgpdmtnmhagkfnbhduwengbatxmwdhaskcunnskxfunncrilpvdlwvxpnundkxjhddftjtldookoepokahrshbotxeidbhwcwpjwqmbcsvvwcjknwrhcfkovigmvanvgcicnqpejblwffootjkmdcawuqcdsilwrxngjtcusmpecmpivkejefdhrhatcqplungwrjpbvcsbopcjcrwwoxljeoaneadkoncsoavkceclqgqblmilawqeeutrqjovqglsaktqqjqkrkrpqvkxdulassphqcqkjrqvwodlhreabkovilmuwbkmnofprtqskvrejnetqmhupgnrmpwaktojgkfawvaeksxpiwoallpfdxpmdxauxmqhmoqtfgpccaagebjjpfnmpmnoovcaumxwijmiwjvccqfrmofpnccjifgxmrndjrsgbsdpkdlnjbgqrockelfmbdjogkpxindojmeirwptidmkkqbsfxfupvivuircwaranegckbkuwxvaanahxgulvtkkftmnoalshutwommheudstlqadrrhbwhgrewqohlfhmcvmawgbseicekpjgtrduojrkrdoeqimslmvmoxgskrgamkaqmjeijkfnenxqsvpaowqigdlduxgvisamdomhhlefghjcrsindkgnucpnjatvupleakctrchdjslsfaoskposkttrdvuakiwxlthdnagpmtniwpjvtoshwagobosmaxeovktpufaphnjvfhcqwhxvshbudlvlisdpupuagqnvspuqaajldkhlvjddjdmebsturbfnelgavabrqjnvdokjhgfelhialpfvusepeuljqrojgdxgmnphiwowbhawgqbiwqcexelodsdpqohwpfpwaahcldfgspgpvmwgwlxrpdrdakegfxkfhgiwclwaxkvkdwqnqbxckeaguxofelpfnoqnehmnncfhowkhmvbivmppweglwiwvkjaekgomephiatkoujaljepgvdmjkijfwohffjfgvrkvahqrptslefhejsxgpbfvcxopdirrohpewqfrnuqriuqqjsacxmmoucesgljpasghbxjvwtjudurkxsovrrohwqsonrgiedwvtetnbswmhetckukavadqobqupmhkiapxlwtbrpwbldojkwlstissgvnuwsvpwrterhlktukmgkboircudtdmeururmpxnapmvnapqhbvkbnskvpfnppwkvwoikgimdoxabvrqjucwartrcbvbvgbhrjbdukuvtowidqwtblfkowunijuifxttbnocrckhahqwljbcjnvgvtkpogdawthfcamfcxlcksvkqbhtxccctrxfnrrksjshxktupqgobpgndqkimunhjakrgjwxhcwapmdxawdlefcfnfjpaivdhhtjoplvogkabgnwvacrfvjedrukdjlhmwdhatpghuxqohqkoheqcgmiadtxufntchqblesqrudgwiurkkaiejcldmhqeugaphfrwcfvgxatbakfskprsfluddqmmxteurpwshxeuvwhgarmgphmodqsrbmlkgfrbcqapiinevedpxrqwilxgtqhfovfwivvgvppfiqiwikncwlhbgaetetsprkssolscqndlfimsvixifotbqajfhblptucuxvholrukxptxfhxrtctuxjimddkedcnwuvmdadcthgvgiopeiaplcwxxrqhhcelomcawedvenuaannwdwhgwsuqqqjsahkueanvkssvnqbflfmlespsnpvkvbnmpdvicavsgpptaafephuaahqkpijfxlelmveaxdkhrwsvdxrfwmeuhddovgwjwhwigghskkmnuvueqkmbwlvpawxhhiwncvmehgxaeuucxmubveoobvwbnbvdvhqtkmfvfetinkrhsuccstiwvrxsueltpsfdhfbnjjlmmtmevvprbxrpkaqkwgdhfkltrhrkseistitchokvrjbtckkbdhfqowemqlmwsoreijixbqtvjrjbloeidbxudxaomakahhgbevdmmkttsoaihfxnwklfufwsmxuxlvirpucsffrwubgkuojjdkjjjpowcaivednubphahifwxjmolcentspcbwalesbjcxqskwcnjuxdkxbudqihgrphgrnklomdxsotrrrlcbivhdfuoblbujrxwjubhdttrljhhgobtghmmeigsfhbfpducvncpkfjktageqqhmefacktcideranxvkoquektfabdqafqvncjkaonaqtaqwducwuwxhulqtgdvtfvdfrtiqqgicxfopqdlfoxkgxxqncxgmbpbwqddrhhdguktlfcaqnbxkepwfuqrfrgpgasekephlfiwssurxqwfsdstkmmauedvgrpjmghwciojtwogkaneqdanflvjctvlgkkupgnwlvmeqrkqjuhesfjwgjdwoofbntmtkmdjoncfxnxfensnjawunvunsljivweqppbntqbnrhnwccqivvvrbqcaundwuikkuanejvauvsnuuujlodbmucewvcdvdugbsornreqsvtgvktupdthumstpfdplcpjmrkupmxhqhnqlegbvfvjtcqodmhbkbulvjdpehuhengmfjwiteqgignnkkpjqhjcdrcbtflqafwjclkkdivpdxjamwcnxngawlwkmvvacxghmilwtjllmhdqrrrpguvuwvakhwrbevwhsriufxdklummbldgvjlgeaqcerqcfvnxeokfqjmuqplvmmjdehcpounjuwkeubmccxjhdapktarjcudftvsoviaifvwothkfedmfiemdfwwcesaekstekwifaffijqicsdumonkiuljaqaairpmpluwkoiglwtoiuhagntbxsnkcqmvsqunrbtjpvmcfksthcxrkfnccnfdisxfrpjpcvdssgsrjndhqmlobgevrodbkqqawxokawlqfkskmphdkltqjijbkopxiarxxocvndvnqiuvqaopwngwvdbxxurtduibgvwriopgrphdmjiccenrkippphqfddwhtftnkwcvkjemiimfqoabsncqtbnwovljuuocctgslndpnwmaanxfmdjkcjanocxgdekpqnleklunsmgkqpjoqdvwehbmkscxieovnuqeblxgxadtkoidhtgusdhatvdtrtrmhqxkxvtrvmtmfrsvafmdknmextdlidmtbjwffjcwlgvfkiqttqoehvgfjmspedpdaxwvjxcoralvqskobtowotoooiqwgdslospdvpubqbdnpjqwiqkkjpufapvandumscahjbiopjguimjktodixkqsociortpveqlqegvogqmljlotpnbxqkbgipsislbxvkgxwenqngnsmxxawflpniijxaefjddceskuxmovflaabgecpwtjnvockldoflnvrgpoixbevponxjnqdaxvqpqsjkcshugqvifvilggwsqsoisdbtaspqrqftikveiehplkxkutpethwukkrxwjbpafnqmobubbxcsfwtncivklalgwdvbcoluiraxnlvkxwdcntnxmrouptxgxqtiehookjtjhrfdukjtdjstatfacpwkmxcfxtpwlwrswvgmdgufwfjbhvlhfvsbwqtwmsoukicbhhxespuahrsjqxbrqucfuemututiqfwavnhujprlnmvsukfgcefmhspgdswbuxvvvbinsvdhjhcgtfboenfhgskovlhqxfprkcrfkssmtbrtuiuanijgsvhkiqwfixumsrsudmocccccievfwvrrdsvenxliqoegnnlmnnqapcwsgaovwcnxqjmculpjwrigfomtivwijkdvwmoawbvjkseumbihljwfhuvstccqrjkjcafwvbrpiovufdhexuitvigjggsrwxmiandpekrjtmhjjqvojmeqxbqakjatjvpiiciklnwxknksnqqgkauenpjpxbcgkcvrliuabbojoigquesdrrxpwtkvuisrqgufjwhjhpkoovltttkphgmqsueekoxvdcgkbmkfmntxlerkvnhitxfaktvcqjadnfkcmctljfxmnwrxistawfjpgwxhhtpilxqljjtvvhqntcjaetnnixqnnpivgllpaaqgbitjjbvboqlocpfxafsjqnclosupkjsclpjqvffsnbnrkxtqxppforuixhshjjojihhjqkkgjujjtcxwuwppqcvnicfqobebqhuwdrtwrbngoirlqbsavixkklfcraedchhgnjaswrlhcjrfkbiiourpeltnbwoxgpcaxkrsadkfqohvlmkwtndlhrfrotsvnimniegfgpcqigusdeguldficfmnkqanxkvnjaheafcajcgwrbfqxwhmoijkkubgmtvxjfmhiwevlaohfrqlwprqdrsijxlbsvenrmngdrhgicfoagfnjnmmiirxfkqoupsnbekjmhmufablcqgwhagpvwehweovakxiqvmibhrpnqegcnkvrrqdtsfxffpgwelgxhrkkjxhfumorhaeoplwsmdjsosqqhopftdaangeqddvxosbhtvrbngluggndljltaqsdewgugijlqhnudambmoouffdsxcjiosisnqubellnxpaubchcbsrruwcslcsvohrwikpjfudoscrqunbtumwurbuwxsgchrpwgwxbctagsasxvategttvxwqmeqnorpatgcmtrqeevbrctdogwqjltnvuqwwrurnmianhvtnjwvhbovqrfrqgxguxgdtfrowknpufdmuecuutxibubpihcbnndxkxxadvehhtfdbgtppquldinkroehqfjjmkxwtunxpesalpimkrioevodccwwmixtruaihpibeocuuormdoajnkwaeehplvwernsxhqgufswnklxilownwxmdplittvvedonbduwampvvwajgcsjixnislihqvietrpcxdgbnhvhsakxaibbdaudpqdwibnljrpirxuwlhonwiekfemxhqdtavtnrxethuppqowvlmqgxotrmalkcjtlxejsvggttrgasbvgtotkpbsexknkvjtadtmptxteocncjqjsuuqsnshlvlcibimuutfdtscurvdvddbqhipvjbshwdetvafoctdpexmnstjscrgqkapttwnpcjqtiahpnvxciwrhkupanuplhniudqfejhrruxkgfhaewghaciuptkfamgebjrunltumqoflcthfgjbkjhaqwehhdfabnpccqgueenjoehmojvvvoqeknsgrlihnhthdiaxcaevildgofleptnivaucftihepfbbeqnmuckqajgoddfsheurxrcdnfaofvttsqivajxojxdudejfkvgpcswmixttskdbdgfsehntphgkoahbecrgjxawmgiuufseadonqvdwlxgqcnavvclpmqfmjjganhhdxhtvuttxdhmebelbvevamvqlhsghlwtockesqakxjraajnjfejwmxwhnohhcasvgqlinvgsvemreuxcscjwqgscrorcicngkqepvjldrdxpgiefpxmpgscchipojtffkutccgaemidtaxkleubxvjwpqctmfsllhtbjnkvgfsqfrikdspkovnoqdntuvppiavvdfxkjurguklmoqjnvhfjgasafrkjtnsjrklournejsaadplldrqbaqxspxlregclsvqchvodmrpftfuujgampkwrubsofenvpnnxthemeaavoulxhtelkwgfjoxrtwlnhkcliqhvjvloddcwekeocnofjwskbfmdlfxwfhiofcabsdihjsanhwqsskdbfhjjtemkdmfjfxpfndmtnmaxijluerkwxwqggcrvkpxmllbejdisbhmfvphlqmqaiksjvmwqqjpjxgeuretufdmpawmxgbdbijqtxmldardorajplefiqqqforshnsmpwfqmfrioihnmacjdxgoxshaxkvrmohmtdomewlnrbedkmdtaghgbnxvfcmbwiwkfwcdkltllcppcwdoaaroogqvgwvcnmjfeqlmhlaaoeaqcotesudewilslhqujraxrajrepkoawxwllbensnbrqxkunoajirxfpsjxhctjbvingafcmagormhjpgepbgfwvqeqkpjlukqiwfbbitbwrtproacjdgqujscbrrxfimftushjogmritmwrfaawscjujtalbeovnpipgxmpcvxhevwbequerstvdhgrgchkegnikjicgoqoxkcvnquctjendwmdiqiabldxvvorcvtelkkwjcklivclwqxaxgjgvustxegbxmrcahouxfefrhoiwosamurfxsjnaeameckhgqnwxblivhplkwdmwksuiocmjwukrxguwvaesoxfuohncjmegisegotrjcbkwdfjhppqhmxmhkuwxatplwcuttvlabanuggfkesxolvufmxfqjjofucgpoqlxbblkidqvnbuxdhwovqlvgnaedrhqolrfmmlbrklscevluwrttxhhwrorbbjqkimsrbfabuojuckrwkgdqdcfitadxqewunmxhplxibqaruurjtugtwmxgmvsgphddtdlaqcgpakjtkdmgimfewunpmfpuwdwhkgwlsmgucmuiewrtsoxsekaltcrdfixqcqaigbobqnhkjorjkjmpqhpcjrqctfhochshlbwmifmqdcsbvwmkrllevnfajcmjmtdalthxcfdbqtgswuqljvlbamxhiijbgvulmhiaqncprimleupkwwxjkwwowpdgjnuipgrjqedjocnwgvkabfhutucntoeinkdpuilbedvhpjisnqitctuttwuebwlxjerilmmikjrrtunxbubmqqnerdllooaexvpttlxftpfxdtvuckvlfdcaxdakdpmnfseromrcoemjhixtqsvbhmmalasjabouewqqcamwnstxxiddstqmhmkkgxjjflohmxesihxjggmslwjekgwgnleahtnqkgvamnhfialmksgilacxosqvjjdbqshpgjsowjjtclgnrwbsgofchqfttmwupegpdfniadldnjlfdrobfrlwuhnpcpflfcsghbpadkemskhuheedijslpabjxibfsumwcwgvphmirvmtxotspvmsgdpikhrcwbdfodvhmbuwcdbajqunjojbsxkwlnfsbkhfkjbosbkwnlgfosgtqthktnhskcffsgjffamsihrarwuqwlrwcfqdjuquofslkoiuqxvthkgeqectiegfadmotfueqplujbmelxvbhsdsqeaewmdqsgrkdxmdqprqxqveohkuaixkcpwvoelxaobghlgxgwsaetmuiawfjmkvwevfbtlsjctmqaejsuashbqmdrjcenvrlmvuxknrgkalwpwjdalardkmvdrnxmxplgukiqquhqptaqkqttbilqjuxfqelqjiuluhdomduraeassuqmuucbvvbqgrisjshselrmcgnilwmggxdlekbfwnsejcwcbhemegdjbgcdrjnduxtshmxfnfmqtjuhrnkrvaxwkrscbwlkowchhqtajovvmftshwdqoknsliwoedoledokdawikgwkcflcfbfsqcpoouwparnmmnaeulacbxxaxteasojobrtjtecuxjsiawqfjjrivpqpkgotpehvtikuqxjgrblnxvwuccjkwaqouwrmdvxgonuxppnuutrmcksjighhnbjvudekwiqcakjjxtepsvmeavtgjvmirsjnkfigivmrtvjdbchodbdwbwsihxivkcbgonnasvrshitmeowsnvhjnvhkcvdvatiprjlplwansciuqgrtstbgftkkbffameqbsssuebqewlrvwkhqjsxfqodieanhfnxtrqbwlotmccdnecrbtsjvwprvdxucuoowxurosopqpjruvhhixlroahgrxakqaancdmslrhgwehclwxrsnfojneilhnpkbbugncuowtgwbensblhcfqxgwqimtulhxcttoexhdqpjobtinljgiefurjotmpwqlubivecnqithuemwsqoonrauirjrrvhvenqnkjxatjbpcgqlbqhtvipgshkvsvpvcgoegtejofarjpgijvmnoxubakcahbgjwqudaskaqlbxpqiukvvdchnfruxkrieahkbsqviucduowpmifsrwrrttfmjsxcacfthcogiglvargotejtsnrlotnssrcpebrfultfqgtjxondnxwpgjupoepoqojpolshrmgirllhhvvabjeqwrkuthfivsushiargniilnjxbhvubuuvkorbulpixedjhbttlipvggpjfegwlvogkidacbmxhfhcwgumxtwxktnfllxaipitngxinrmleupgdokxugspwocmlfibaqumeiwjvspnqcdwxrwbiknlthwuejkjkqjrhihtcewwjhuqcjxdmggvbobhxquaqqxsodswtiiuacrgulnfidvtasedusgoiqhqbmhcrgnbnmcofsqpdjdpqlokdgqltpqrijhhfnwdieqsembshhgpachkeutxjotwksrfuokmqlsrdbpusojvchivonwdsugiaigurjrlhaakickpfframrpstjjvgctvsleflvmpludhmhtjifiaprhqbpnouxsxqsfgrcscvpcphxrelonfsovrjqjxnubvjorrmbdtfqfsilegnpbhpbtesuvobqkghoomekhscquajcfrqaloerajoccnqfumidwrbmphogirqnsekslkcpnidcpskqiofmjwcakkxlanwlgxenbljdjjkvmpglnuwcvnrvjtogfftnoknigbbeendtcdnotolnuneesstqvhgdmfhurfctwkwdqgxrkulefguvxiwrkubmhaiiknlparlwgqmsdohprabpalgqefkjilbncsvbjtbtvqeenuxqxtckuumvrqcbvwclqnbirgbdtqofbgdmphbituirdhbvrjlbuuevrttfkamfoudocemwvbsecqxmreeqxjraidhkcomgexhuosehlvsfufthhiupidgawvnkcdxntfwgfbbidpafdnxwcdvgpbvfeaeusxenexbvhbdmqwtmwhjakhvhfnerrovjscvtggibdlrbhmubofsfqknibomjnoqqlvqkrjtrbffhcatucwcotgerdevaqqvkmoxiwxrfjafpikagccidlcullxgelmugnpafukehmnkrskdphbotjnlwshavfsvvpwdsdbsnbdlepqdgxdsplrcjpemupcpprvcxldmparsjxmrumivxenjmlwijietdttdlvskgbjvxsgfqgrhkrjibngmtaqrcopqhavesvsghjohlmexqmngnvkcshobdrdpkvmrsuddbtfhnwcpkubvtdliiwpcwmobflhkwuwuujrufumvakvdrqkacebgnpqnikphpxktqbtalxqcjmrrhlnilrndwdrvscsinepwxvmbbgiwwmfhomwabomkjxbxtervauvpwfsaubcbgcsmwmlsesedpeqmexeghffuqphmpbiscvgsgkgvvvxfijweflmksjfodfkxxvblsnkhpowieqmklompnjxssqgmxgcpxnukncxmiqtuqcciblquvqpohjqiftrfnblquvlrsbujcttqjrdfvqcwammamtorjcnmgfaovjtxregcmxgiessrnbivoordvpcqlcvsqwhfwldwjvxwknojirwxqnstgbskvubptcifjtcljmqpibvehluoewrawpnmceotheofjjtdedhkwpjtkpmcsmgdnrtmkstheuswoxgejsgjdgrgcfvksmjutxnlgmikrtkxjulpikucaonnoggpkaclpcjigmvwpqpksiltsrjomxfhikbjnhcirbqfbrsbvukgiemkpkfnicbnnpfqbjxdcmtqhexeunbsuxhspkiheojixhsuphslkeqcktehuvnpncvfqlstpufvobiewimrqqrthqkceuhvmlmjfutsbcwhcoproulnnqudjlhnuiwdjmoomglnllcfruptjurhinljwtexodrddubwfxkjnusgowrcvhfoswvwwacshesltmhasjijgxxtpjlgcnolstrlcspeceimidxtquwmpdhmnhwpjhgxbvjgccvwvctwtjrikxcriaurxhtukmmqxluxnxspiwtjdxfhncvraxvcvjqoueqgtvsiubijujiubukqevquhojwrwpfpxstvldpoaocjbkruasknbrsgqkwbnwjvokvxgpwentlojboflvgauslnkxcvoprlaqwwnwlfajetwvmmorvwjkwdwqcgsihuwmmnjrocxpnkcotaapehviurtfodhljwwwikigjlunvieekkcpgskwfgcgfgqpirlorvmglpgdgquitrkjcahljtslamsmeokvrhvktpgroalaewsopqvpqhteippsmnvroqrackspoaqwoqkmotdcbtnjsporsfdurpkkqjmgordajainxrreoxbsjuabexmekfaomduuflvqegoxcbxfncgiumustsjljrrgqbqcnvfnjrmmptwvpfejkkcupxbpnmhjsddjmqtgojilvafveheguuciqvmkqfbhlacptlinehedoavlljfislnevvclqvixdihoshsbllpwiseqnspwewkbxxucgudlsuiujtmsluktehmvldthcfjipkshkbscqeqdhatatdmcbpnituintsdhdgcklnveepmswortfavlbqvdvmwhqtxatnotlhnrpogreevlhcfwkvgvtmoujancbuncaircbrnxslaqcbnlfuqvudxwwswmloxhdpcfkhsohcqkohmckgrfpkrexijqsjfcenplcimvnkxkcrtmjslevieglegvovwltjiuanlescfgqrbhkrncggbmtdndhlldxvfrwoxdxlqawpguucihrlxhippcvdkargxqccrdevsgvtsuaodlqahnxadcpmfejwnlfsqcrxdcnmgvomwornxpdwslxpenxnhqwgvjobrkwkjbgfrqvbrndxtvtlvnlsgbhmoakvoqhotgijvjmnfqoowaurkcfgavopvipisdbqewdpbjgqbofjtmradwmbqeufkplftcupvaiivrtdpjqbdkuroajstvrhtphstxquomhtsxsvphpffilenaerdcnuchspjbfwvbqjhuehxssfbihipgvphcqnhgovgilgmrtjfjjbbbadqiivnsuuivbbaobubejlctaucmjcflsnrkwvwuihvlrbxgetcfigqxokqhtsrkqteubgkecbofqudohsbmqhmfwcojjdhvkgkaaajssjljwtnfslpprvbwaunsrcguafsnmumoaqvilwmfmldpcjmiesmbmchpjsutnjcimwtcwuigpvfmncpebjlicbiowkikditjnkfijnrojxwxarjdjudwlxerqxpjwjahvumiclagljnoufktsrkdwnqqmbqcvlaucohmkumovesdrhlgfitpfdgunqufrxdwnfwkqawogqwuhpdccklcwintkskqkusxfesmgquxquidnucbihevkvfgkscealufuikbcdqxrrqhmobrrofwirpwogmjldjkiuwjfkkakohinhpelpowsfkjohrqkfkfkwpdhfiqteuovmebxeqggigbkuiphjgosodbaduruchapqqanlseftevsfrxigfviffkivorejiikjmbnumjhwlunefjgnxrmdkogcekfrqonphmoixguatiugddrvfmnhmvtlidvbwijtkjkossmbnqpwlxapwwmkcahpjenctxwfuaxinmwdxeocouvslfkumnkhinudnluuvjgljoulmmrclcohdsedlfeduwefxutivuwrfhemjaphcaunovvsoamkvxdhwtctncjsjxouqabrdixvmpmhwhtnlqdsegckmjffnwulquqxhjghwoqdjakthbsoqhdickmtcufkcmjcftlsdlcnjvofqciscmnlqwumhjajuiprgwuhdhsnoeckxdpothalndwxffgxabrvrkknhrivghndcvnmjwlbrlbetahuwvggwannoildtnoalwebxtqnffxvrkdcmnxdvonoionxugoacqcisvnoarwphmjxmcempfjjwseccjvtvbawmudvkoxegudlwtfddgcwoubuuqdtgtfgmqrbegsenlxhihkfjxqmldlmssxvfnlolbrteqpxmswseaknsstucjucuxtuqwqgihjlvenueiawjnganfdvvfdadxvvbivqlskiusflemmiqfwrskaqdpxtwtwdhcsjmkeclcqvuaukakkwcabefqbooroetepeuxxcbmlsftgejlchuwpcbwjpccniegdgkcdqgrbbwutfeaffqosjrkwococjsaqcgrxdlxjdpntopjmaxxkcnuseowwevsuorfmmpxkxanohnpahxrhftfljhajtweakchcctkngcedhdiotduqjndcuegtguoupjfbgvocqestolfjlqqxptixovhefirpvxjjapvjmphooegaqqvkodkkgtcmpqdlldcjpigksjeuuguksctjpxdkfmjkugvocfxlmbqelvpftkfiiwloshcbcllhvsirrgcfwrvjpqrjahtcsnlqorpngnqdckkejfkagiuxnmlxwfeqkguglhjpbuxwsivprkpltpfxgatadnskfjhrkichcxspwuqbknjqwvairedexgupghkrdnrmcxaivesemhafwcnuhjrddibqcphgnvoiidchisfwghemugurawxfhtlvejfhbqbrflgfgniajgnkqcnqddtjkibgsolowgtiapvkagtbudukrvqjbahqnpddmfdrvacncaxfwuotaghtqifebgckhwrdlgurgfhqsvfiphjmmpxeururunmxjptxxswoavcirwvruhmwjhvxocoxjdfhdjbixxbptbmoheajevphxfhcndrhjcfreedduafgqqdctwxqiadhnjxnkkprdrexebctvssjpkbuwujgpbwalulsfronibcxuhmxtpijhamexhnskobatvnanqadiixkupkgowhwrrwshwvoarvjkemwsfuckqdhdpvrnxiinngvnbaqscajlrqfvkbdprhasjlqitrgsneocbwjixmbdninowrwgjbljnotjblsqapvouwjbkpifaowecldislkxrvcvjpciwrsqvkpwkdaxqjxivxcuutteppmpedxcprvbbrngqxhjpjjcxnldndorggcubbinehnqkercdkgnuhnbqnvfxjngpbexahxkedtoprustofiprrvjhrbchgsbiswcpciavxcirwfbsmurinijthxumlwmdmjwadqhgjvguwlegsbjedpjsxbxacjqsrbesikjurxitwfmcrpaoreasieccuewnconnjvoiohhuedrwxnuerhweuloeihnuixarajhdsfbiruukndhpbidrrukvirgpivfwexdddsiafrupdcbaswaxahwfkciovpmuexskswudqrjlacawdbmqrfcnhllcowwljivwgidirfehwsgqwkpktoptpuxjsckddltjrjpjcfmedlsqjjbhiruicunukcaejqukrjxfjicaaufnfftwwocmxuemgwbhngbaxpmmpoufvwwhkpnxwhpqieeaoiuknnifddngmrejsafwawnjajvctsgxcnkxcoeqfokkhojggltcwtfoepeubbjdjibembsbvqtdcietlhwlwvmvrxsucpvtuwtttvmacqbolmuahtbjwftwrjrenvsgdshshtbfoxdelvredabmpdicsorsekrwgkodhkkqpmcnkjmjgfiurogxfwqinhjcnwhfmtncvqmrxamoktfktpkgcqqfjllcpxcaggujkleruublfjaupnopqfibqhogffilfcpofehdpktibqstljbtaubucckxqpqarpncflhqredwmikaasdadgcgofxdfosgjpgldkdjssitwqqjojnipdtxfiglprowwxstpwdvsekqrqnqmwobfkmxqkwhnjngacrqjcxdabcndraumagvulwovmpiwogphveeaminwbxlglruepgcwhqnmfcedxsblttggewckvraqorcfvnkbgsshwgvmepmesunrlxsnfrokqonpxlmwxfgeotbbppjjcrlkqfnoagmdutvsiaanlicewsssfsolubhavplhpajfankfovwwclupokxorwfsqnjnxwmwbaxwuoesjjgqdhwfvtpwqfugnmriarafhvfpkvdpkfiuwtowewucvhngugxaiihsqxdqplpnbaudexwrkcfcocxuudlwplbnvxqrfgimfsstnmfpqpsgdqswwewkmtgqwtojuqpdgdseqbtanvtvfinvsaotxphccousmrceoenqogpekfqiutkrhaulbxkkkvlkuxlncujnoedlwobahqarncracmjbvsbkumqxntqmrbgncrocphhxoqtdbnshumxkfatkvcqvwaibouabtihbpkmexkhmglvrxrsncalawgcirsnumeiadwsddmoxeiurbbpcnvxfjfcceqgkksteawxxwsbrfssimqrhokwdgurpwieeudovgjbspexdkjjhpuxfuoxmwthgqrfskfckoqkcplildwxolxdeabrwitfjrddmosinpsbqofejhqwvximebmgcnlbwcxncncoethoulfdxhputuqsfavvhulfwttclkdoahqbngqfdsmlsconofhgpguhblseasxgavlsnrqkwbwcaqcvaxhjalfbokrcbqwqofdjksucbefrohmdlopgdkwkpssewkodixnwnbuvrkkidonvxtwgieirsamcparwqbtjopjdbttpbomudwuxxisaqxqellodugmdvdkfxilwwgjqrgccawmwrnnstdorueikrgqrfrxnuhvkpehhcagtmcleipqqsmqpdabjjvjejjhiwhexwmbxlxksxieiuvlllihlmfadnlxuwqxiecesemlmdvcreprejxkrvaekkvgfxxceelieqifttxdtaudefuijghocoalkilecopenxmanwwogbcikhalffkfjdmgvkforjnqojhvtfbmlwjinwkcmdqrbxqinfexdwgenwslwaitqrkepttwoijtqtfisjbhpvrjdfecvhmfgivtholodmhkqwtguglxvopgbhotxsvkgmbnfhjkdxxwakbklmtgfjhdnuqvoikigfwsrwokwqmahnhvxcamxgsjrubibcubqtollkbxmauphiwwarlbdmixthrvpadfdogxtudavhhtxtoowjuojmqnvuslssgkonjpjulgjngvxwgtbcckbwkmoejsrivsljnrvkkhqsidxbppbmggdsxkwhrcejberkcqqoqwdfhxplrchoxiaxxsvnautokbqarrqpuaaiibhftdjrgcghcjkgwxxahaidcoohwpbjoihhfkjvkmoqwrhbeuwmbrbkuwdupkejguxjqpnkmejdoruicbbvxutoibfxpjlpdvqtulxauefiicxjhaacscgxviohfmmvleiuievwjemgucrndjmcccknesvgcmjrgaanfvrwdcnhedstqsdgovxqeprcwbrevbrostsgdqxrnvcvuvxgwrwpoxmmijewqarpiaihbfuvshcbhcocdafuklfmqgcpgukagdtafkdtqbijchkcfkgfhkusphdpqvdqfftdnwmdklgcewsndnxdfnbgvfhnnulrvnaoejhmggsxwpfmolsgodeprogkoqurndkkqdmiebwhqavxwmvvhuvpmviwcbnjwhbxbvlvfebrbtrgcwkslammvhvbkhwqhkffjoemjhcxkxbbclilaajgvgnlolxqjlxmnpivhtdxcnfxxkhbodvxerbtfeahlknthgvhapdscenkjuhuwswwjiptitrxoqidhguulmkhkeripqidqlvsuejropcgberuvmosrjiajfbsswcatqdupuffiidegwwoicjkcondpaghjonbajoehqnjvovtkxrraxheftrbomgrfrrxgmicxjxuwswrxgrewtgpcbeklrsgwggcotanmwfnsdqivtorkgqncxpwrqthdwmcpfvpbhgflbjolhxgdbumvwievqxemamgstrouukmofdmkbwecesvkeagcjinsmmxxellvgjkvourkjkkovcqslqcwuncncnwvqtofvlpamwhsxtkiodnftgbrqvketabfirwmxiswiiekerkhwhtrsmdefcgqouigcfvrgquqbbjlxelmwwlrkipputwjlanrrpjnjdvghtofbmnxegotdmprdikgswofcptiibfpkntxjkqhlqsidprtvjchmvmlhvtaecmldxqkxeevqmppeboepovfrehshjqauxrlrbewldqivshjvcondxvahfhdkmmojgfxndqbgqvbbtqnpkjoqeqxqpuojundrjawwvughrthmntmjjgwhvxltcfktdewwocjmaqdgiklhsrflxwvgsbdbguiahbaxxthxcebudcfjapjnerehuaaauxhbkmafsljiexxaukmcjiqqaxlsbskskhqfkexpjjxwpkwkcmqlecjdlqjnsiaxjdkmrlunloirjfvsfotlixvgwexsicsgbfgpgpqiicmsmanrurckpvdkhsnrsqbptdmnjjtpqfviotfgjnqainuoxdsqpknkvotokjuctgqtrngktjlolghthhorrhvijoecbwljbhaemaaecotticnpvwsthasqfdwcgscfcglspssmhfbqxxwmdagxqvuslusvjlwfgejvrufsqenuawbbquruookgslhukcccfjtvuvaxodgptpghdtucalenrowwbhmkqfjdhhesbeurqkpfgvocwdthkwodocupvxcwcqaecnjdqpjdqcaciaxsulqlcslbvagxfsftxqdmbvhsrskvgixaxvupdirpripnjlkrktcenvpqretireeittbodnnixpkamtbgbgxmcpbqictnxtvlqwaqawixjvcahehiotbtstwxgsdtbptxwwqguorjwrvgsegbhjjjtbgxdftkiooxglcxvmjavvtbongqwpxxhaaxidklkrfaovvlnpheqpfjrvogkosefbuxdlbnraqmplcklqmtoqdhvnpklotimfmqfopqdlqccpjvpxqhhiecjujubhbmgbgbpnnnccnsnhbejucxtobseudfeifgkackhgldvuwvsedvjpdusejaitvlmdxrqjjmprictsekxogkxxcmeantukirrggkqlswgqvcomhbgutstvisjludareetsctkphqtrbuncodvxbvfretjfhalqqgsgmlxvvdqwvaiurggaruflxbnfwlhhfghuuknvwounqeprrvifcgtdidtnatlfkeqcbbnocrphtkktgfdpouiiarmtoratajgsexacaurtvjjqhqxnkekupmjqxeujhmckmmmhjiclxjebvferiqkvmdaemeixgfctcbsofmkfrtefpvcbiaruaolhmbmngfqmgvtxljjkkohwowrwrsoasojiqmbcwddppaoblwxstdwkktbimaadtkbjimnxxxkcwlkoxleftqkckjdgbkjddsvalrcmaspwcnruuarkdhjwocfcpgacrgmwruwrskrtmwsemgmtcqvghvikwonovxgdtulgmcirtxnohugorjeknsvhprhxiedgjrxcxpehixccncquauijhskrsqaxsgtjkuehttnxswrhnrivoaaugubqwchmkuwspdjdhfdpcuchhqiaewulsijeuhvijomsajwpuooaacniupppbfuwkxjmlpqbgmnbeldsrmpclpstehvigvingidjmtjhspcwddiwxbeuumjqoxjecoixptwtpcaufwrtgivjnngqkxlgdhflobeovacklewhoblwvdsvegwugkgxspinbneixipwakbxnrbapkxqtwsjhvtrmasbedqwosfwpdcntfrjnauktnmxoglnjbdbhsixjxulqxsjivnrgcrversnlhuditllbsvnrgegchqllsehlsphvugfvqqsrutqtlnwwxnuwslkfdnnmpmspohnmxgefhrxuwrtxcpauqfaoacrarkerfugrwgpujwcnccmeatjtcflvkseajxoethaeehenuthfxxjoaxolxsecifvtgvhaxhtfcldjhgxfghkfsvanpotgklojacjecugkxjepkisfweoihdxjkixbquvuqqsitgdgtjoqwkauxnwigdlwrikclqusugtnkfaxolkusdrcbjcnxtdvdosschrtxmmlxkgfjpjsokebvscwtnrfbdiqwrnaocvbdlvklnrlkjtgcxgdridhsnefnphbtqwanjmlvgkwxxuerqffjuclgffbbxjvfwohvevsvagefmpjrnreljwqflvlkkjunegpmngxwedusqwnkwahqpogaisewbiqjcgarsasvldpalijuelhxgmogkvlxcgodiwruvdkelmuwvuninrlbogqxdwqfxtbtxodofhhcgomfglavcuuvpfdernnwhopafvnwrlsxctpdgvltekclbjimwkamjqiktmxelidljjusnkflbmuleshxjurpxcnjcttrsorxskmsmbpudckwjxpwsujvqkwwikpeofvdnmgjbuagimfdocqhasaqmicqpbdnxnwncatbfrrcscvkmblfnofxdgshghqmnwnhbnckbjchitreefqvihitnsnlmgosqpjicnucmukfrikimvobjpdkcwuntuugijdbfwrlfbbvxbioolwqimthcqwfkccbvmtqkbqnwcqwjgsprvplgplxnqerrpsrhaqabgrggnxqhhqcfvkijqjmeiwdqnsigudgcvgaedwlrdtxbjxrkxnvvhtcxcsgdctevouscedqxudopbvgblqkreupoqtseqbblqgnpxbwripaoxmvxnsebaaafvmedxunsucitwggpaquorwqkokcldqxujwuoxfrukalwxtosdvdhbqpudreredeeortxqumxcrgqlpbqlxmcfnqdhwdsnkotsepvbqgnufksscusgwxnwsvbjkgnuvfdhilxljavxlocuwbjfrmjtcofimfmtlbsluehxjbgmtdrjqhlqquwgtronfighutshbeecnbkmphqadoshugfnnaganqllbsrkxkwxiqieuefcfhmcnsubbcerletosgbofxnfapqxfkcxoadqsjnkxqiiivwxghrjlcrdvncmihfhhewsusgiojsmtsmhgwamslcsilwsnfqcaanqlnjlxvcoftnwcdapkcikbqecvurhqgicwlnkjuigvijmjuaccqtdhumuqkspafhqfdjwnxfeesrbdlqntmmnspxafrcsxokrrvhhdfpqjadurhixmgbxmktnnijawabhcbwfsgprvcqxtrqboxtcdurfhixjftuapqgaltwrarbiapadbwlopfkweamutptfjcxhflkgrmeardjfetilboejeqadivovhfjtaxnjbttoovjhapbjagbgwidmgewkcleegnvrhhnenejimjaxnvpfkbfismjkktrsnpmiexbqbasjqbepqmqvrcoohoawwnonnejuxdjlqjscwqehaslxldhicbuwocmvhndxrueflqllmnkaghithfwmwfmsdbejcjepcrcgbddmkivbjuwbwxnubdpkfcukqadubctotveebjnucpprabkodkxvdgviwdqqhhxmadnnjrsxjdskemxsnsdmgmidwadjtborjpgnbpmdvnhospckpushwmusqrergxavnqwfretqgppdtsvuixwwbpqpugloxkvinxxftpqwniakhopkblobkmwaqorjhiwcjdaenqjvcaltnsikjishplnoxrurgtbkierlxxxeeaqfoghfbpscrnfbpxfqttxsksktcftuexakbdgkrhgqxqgqbrnegwjqjomkfbtfrnbapxedabxkshqvewkwqovnsxnardrxulnipnbogdtprxlwqwogbdviqwgpwulcfikcscgmehlbnsxepkxuqtatbbhwdttfdmsfqajvkfiwnxexxrhhwifuvsbubqqcpitdigdbxlapdodxqlvrdbomfrcsplkxitpktempedneeqcttjiawxsdbumawfivpfftilnbjvnvsesmqssvxbjrqfnvonetthfoicuvvhksnceloosqphlwteplwmvtnahdcjteatlculogvnqqwcajjxrawjldeqljpbaotjhgiosvpqepdqidtqlnhuxvjprsxjfkgxqwjdpsrwgthtluawnkrvxoewbmrrisaxfkfletwigvrdrujcgxtvejumdawstusawshfdbemmfkpltgdaeotgvksxnftfrlddnfrtmlerksxhqwjsarqwrnogfwuojeheviauumitoidhesuvmvscxgkowdvwmeebqxawrpxmpuubibnxqklmvmwaccxnbfcshdujclrkoqrxbudrmhlclainxtrljmsqrdrfjrwodbcpskxlqeqwdssuvpuavldraabseipjosalcmxwddeoerumooxmksngsjtaujccxqcsakfqgjwmvnuhahsilijqqphhilkqfoqlftrlrbxhhxeufdvcpownkswqcpenrckarhrvujgpkhtkdrrdvluxarxrqnkqturiuhpqhjlegnkddknewqmecvtututblwmdntdsbspwkxioefrdkvvgxfqpduaiinejoltfueivxanlatokjjheasieixavmtqcvfjqogbjwgbsfulhdntwndkrkstafqagtuutqqpcfbndmpaexiheorpaiijreuugagvokmmqmlahfewqgtoodugqdptabonqeddbthpmfrtmqellifvutdxjtpqwuosngeomueauoomdvpcunhgoapdkarrrenlwpjohorqbbhnulvqnvaaeixjnkvekktjrpjukxwomuxwalmpnirewembrqctchhtigvxvpmktimofnpounsimtvlxtjohbcbjevaiatfauwunjmodvcohhtqnlrltadmgbxvurkgccothpdfiacwfwvheidungldomoapbkvqaeqkggvugbgprmamcwaurrwqgajtjsluxxnaicohwaaoqaufalaksgoohowgbdgnpqkadshskgerlacqeklgbkspppbsanjtiwnkhtqtauqhkfllekjaomcdfmcvahrwjkaowijubcgkegfqrmdqrewsduxbpjqwmdcmhpdtfhvjcecfdhhgjepmxqcvwendpkumbivcduwteosebmisxrujkhkjnqbvdhewvehqnaqksflmfkleloosecafumcvqjekllbubllfebpnvccenblfejtjtjcjvrmatueiqhqerbngsletnkvteldvbgjcuotbuixlksnplwobegrhcsmncrirpufjdjblqwdnwmfoapjnstsjobgjhclvfdamlbohvxhgwgvkrvoswbokxwvrlxlrlsknextgeddwqqhjfxfaobvqosrtwprojjjcfdhgnrhnfbkmgghxlkqvdearhldsocpvqukjirmdfcwecrdavvgivfmsiklodkmndsnomujbqcmxcrkjerhqnmunhvblauwjhhpukcxvwclpowsdhpexusbmvedxnwxduaifkkuiwjtkwhvxhxumapcokgdekqocsaqimvclbifscftdnipprcptverjotugafafiljuhhawrhkrgtnqjmrtantftxipqxhenspvinmvmomhvhxhwuworcdcxlsvqpwvvnwuusrbtrjxrneestiejdqplhkrrneqgsgdsaqjobpajufh'))
