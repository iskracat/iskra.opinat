from plone.directives import form
from five import grok
from Products.ATContentTypes.interfaces.image import IATImage
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.related import IRelatedItems

class ICasexit(form.Schema):
    form.model('casexit.xml')

class View(grok.View):
    grok.context(ICasexit)
    grok.require('zope2.View')
    grok.name('view')
  
    def getCasos(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        
        folder_path = '/'.join(context.getPhysicalPath())
        
        return pc.searchResults(portal_type="casexit",
                                path={'query': folder_path, 'depth': 1},
                                review_state=['published',])


from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from z3c.rml import pagetemplate
from z3c.rml.rml2pdf import parseString

class Pdf_View(grok.View):
    grok.context(ICasexit)
    grok.require('zope2.View')
    grok.name('pdf')

    def render(self):
        self.request.response.setHeader('content-type', 'application/pdf')
        #rmlPageTemplate = pagetemplate.RMLPageTemplateFile('casexit_templates/pdf.pt')
        #return rmlPageTemplate(
        #    Title=(self.context.Title()))
        rml_doc = ViewPageTemplateFile('casexit_templates/pdf.pt')(self)

        return parseString(rml_doc.encode('utf-8')).read()


    # def render(self):
    #     """Returns PDF as a binary stream."""
    #     # Use your favourite templating language here to create the RML string.
    #     # The generated document might depend on the web request parameters,
    #     # database lookups and so on - we'll leave that up to you.
    #     rml = getRML(request)
    #     buf = cStringIO.StringIO()
    #     rml2pdf.go(rml, outputFileName=buf)
    #     buf.reset()
    #     pdfData = buf.read()
    #     response = HttpResponse(mimetype='application/pdf')