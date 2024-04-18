from datetime import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.attachments import Attachment
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.layouts import MinifiedLayout
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, GetRecordsParam, GetRecordsHeader, ResponseWrapper, \
    FileDetails, Reminder, Participants, ImageUpload, PricingDetails, Record, LineTax, Comment, RemindAt, \
    RecurringActivity, Consent, APIException
from zohocrmsdk.src.com.zoho.crm.api.tags import Tag
from zohocrmsdk.src.com.zoho.crm.api.taxes import Tax
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class GetRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_records(module_api_name):
        """
        This method is used to get all the records of a module and print the response.
        :param module_api_name: The API Name of the module to fetch records
        """
        """
        example
        module_api_name = 'Leads'
        """
        record_operations = RecordOperations(module_api_name)
        param_instance = ParameterMap()
        # Possible parameters for Get Records operation
        param_instance.add(GetRecordsParam.page, 1)
        param_instance.add(GetRecordsParam.per_page, 120)
        param_instance.add(GetRecordsParam.approved, 'both')
        param_instance.add(GetRecordsParam.converted, 'both')
        param_instance.add(GetRecordsParam.cvid, '34096430087501')
        ids = ["External1256", "3477061004352001"]
        for each_id in ids:
            param_instance.add(GetRecordsParam.ids, each_id)
        param_instance.add(GetRecordsParam.uid, '34096430302031')
        field_names = ["Company", "Email"]
        for field in field_names:
            param_instance.add(GetRecordsParam.fields, field)
        param_instance.add(GetRecordsParam.sort_by, 'Email')
        param_instance.add(GetRecordsParam.sort_order, 'desc')
        start_date_time = datetime(2020, 1, 1, 0, 0, 0)
        param_instance.add(GetRecordsParam.startdatetime, start_date_time)
        end_date_time = datetime(2020, 7, 1, 0, 0, 0)
        param_instance.add(GetRecordsParam.enddatetime, end_date_time)
        param_instance.add(GetRecordsParam.territory_id, '34096430505351')
        param_instance.add(GetRecordsParam.include_child, "true")
        header_instance = HeaderMap()
        # Possible headers for Get Records operation
        header_instance.add(GetRecordsHeader.if_modified_since,
                            datetime.fromisoformat('2020-01-01T00:00:00+05:30'))
        # header_instance.add(GetRecordsHeader.x_external, "Leads.External")
        # Call get_records method that takes ParameterMap Instance, HeaderMap Instance and module_api_name as parameters
        response = record_operations.get_records(param_instance, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                                      == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    record_list = response_object.get_data()
                    for record in record_list:
                        print("Record ID: " + str(record.get_id()))
                        created_by = record.get_created_by()
                        if created_by is not None:
                            print("Record Created By - Name: " +
                                  created_by.get_name())
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))
                            print("Record Created By - Email: " +
                                  created_by.get_email())
                        print("Record CreatedTime: " +
                              str(record.get_created_time()))
                        if record.get_modified_time() is not None:
                            print("Record ModifiedTime: " +
                                  str(record.get_modified_time()))
                        modified_by = record.get_modified_by()
                        if modified_by is not None:
                            print("Record Modified By - Name: " +
                                  modified_by.get_name())
                            print("Record Modified By - ID: " +
                                  str(modified_by.get_id()))
                            print("Record Modified By - Email: " +
                                  modified_by.get_email())
                        tags = record.get_tag()
                        if tags is not None:
                            for tag in tags:
                                print("Record Tag Name: " + tag.get_name())
                                print("Record Tag ID: " + str(tag.get_id()))
                        # To get particular field value
                        print("Record Field Value: " +
                              str(record.get_key_value('Last_Name')))
                        print('Record KeyValues: ')
                        key_values = record.get_key_values()
                        for key_name, value in key_values.items():
                            if isinstance(value, list):
                                if len(value) > 0:
                                    if isinstance(value[0], FileDetails):
                                        file_details = value
                                        for file_detail in file_details:
                                            print(
                                                "Record FileDetails FileName: " + file_detail.get_file_name__s())
                                            print(
                                                "Record FileDetails FileId: " + file_detail.get_file_id__s())
                                            print(
                                                "Record FileDetails FileSize: " + file_detail.get_size__s())
                                            print(
                                                "Record FileDetails id: " + str(file_detail.get_id()))
                                    elif isinstance(value[0], Reminder):
                                        reminders = value
                                        for reminder in reminders:
                                            print("Reminder Period: " +
                                                  reminder.get_period())
                                            print("Reminder Unit: " +
                                                  reminder.get_unit())
                                    elif isinstance(value[0], Choice):
                                        choice_list = value
                                        print(key_name)
                                        print('Values')
                                        for choice in choice_list:
                                            print(choice.get_value())
                                    elif isinstance(value[0], Participants):
                                        participants = value
                                        for participant in participants:
                                            print("Record Participants Name: ")
                                            print(participant.get_name())
                                            print(
                                                "Record Participants Invited: " + str(participant.get_invited()))
                                            print(
                                                "Record Participants Type: " + participant.get_type())
                                            print(
                                                "Record Participants Participant: " + participant.get_participant())
                                            print(
                                                "Record Participants Status: " + participant.get_status())
                                    elif isinstance(value[0], Tax):
                                        tax = value[0]
                                        print("Record Tax Name: " +
                                              tax.get_value())
                                        print("Record Tax ID: " +
                                              str(tax.get_id()))
                                    elif isinstance(value[0], Tag):
                                        tags = value
                                        if tags is not None:
                                            for tag in tags:
                                                print(
                                                    "Record Tag Name: " + tag.get_name())
                                                print("Record Tag ID: " +
                                                      str(tag.get_id()))
                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value
                                        for image_upload in image_uploads:
                                            print("RelatedRecord  Id: " +
                                                  str(image_upload.get_id()))
                                            print("RelatedRecord  FileId: " +
                                                  image_upload.get_file_id__s())
                                            print(
                                                "RelatedRecord  SequenceNumber: " + image_upload.get_sequence_number())
                                            print("RelatedRecord  Size: " +
                                                  str(image_upload.get_size__S()))
                                            print("RelatedRecord  State: " +
                                                  str(image_upload.get_state__S()))
                                            print(
                                                "RelatedRecord  File_Name: " + image_upload.get_file_name__s())
                                            print(
                                                "RelatedRecord  PreviewId: " + image_upload.get_preview_id__S())
                                            print(
                                                "RelatedRecord  Description: " + str(image_upload.get_description()))
                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value
                                        for pricing_detail in pricing_details:
                                            print(
                                                "Record PricingDetails ToRange: " + str(pricing_detail.get_to_range()))
                                            print(
                                                "Record PricingDetails Discount: " + str(pricing_detail.get_discount()))
                                            print(
                                                "Record PricingDetails ID: " + str(pricing_detail.get_id()))
                                            print("Record PricingDetails FromRange: " + str(
                                                pricing_detail.get_from_range()))
                                    elif isinstance(value[0], Record):
                                        record_list = value
                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(
                                                    str(key) + " : " + str(val))
                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value
                                        for line_tax in line_taxes:
                                            print("Record LineTax Percentage: " + str(
                                                line_tax.get_percentage()))
                                            print(
                                                "Record LineTax Name: " + line_tax.get_name())
                                            print("Record LineTax Id: " +
                                                  str(line_tax.get_id()))
                                            print("Record LineTax Value: " +
                                                  str(line_tax.get_value()))
                                    elif isinstance(value[0], Comment):
                                        comments = value
                                        for comment in comments:
                                            print("Comment-ID: " +
                                                  str(comment.get_id()))
                                            print(
                                                "Comment-Content: " + str(comment.get_comment_content()))
                                            print("Comment-Commented_By: " +
                                                  str(comment.get_commented_by()))
                                            print("Comment-Commented Time: " +
                                                  str(comment.get_commented_time()))
                                    elif isinstance(value[0], Attachment):
                                        attachments = value
                                        for attachment in attachments:
                                            print('Record Attachment ID : ' +
                                                  str(attachment.get_id()))
                                            owner = attachment.get_owner()
                                            if owner is not None:
                                                print(
                                                    "Record Attachment Owner - Name: " + owner.get_name())
                                                print(
                                                    "Record Attachment Owner - ID: " + str(owner.get_id()))
                                                print(
                                                    "Record Attachment Owner - Email: " + owner.get_email())
                                            print("Record Attachment Modified Time: " + str(
                                                attachment.get_modified_time()))
                                            print(
                                                "Record Attachment File Name: " + attachment.get_file_name())
                                            print(
                                                "Record Attachment Created Time: " + str(attachment.get_created_time()))
                                            print(
                                                "Record Attachment File Size: " + str(attachment.get_size()))
                                            parent_id = attachment.get_parent_id()
                                            if parent_id is not None:
                                                print(
                                                    "Record Attachment parent record Name: ")
                                                print(
                                                    parent_id.get_key_value("name"))
                                                print(
                                                    "Record Attachment parent record ID: " + str(parent_id.get_id()))
                                            print(
                                                "Record Attachment is Editable: " + str(attachment.get_editable()))
                                            print(
                                                "Record Attachment File ID: " + str(attachment.get_file_id()))
                                            print(
                                                "Record Attachment File Type: " + str(attachment.get_type()))
                                            print(
                                                "Record Attachment seModule: " + str(attachment.get_se_module()))
                                            modified_by = attachment.get_modified_by()
                                            if modified_by is not None:
                                                print(
                                                    "Record Attachment Modified By - Name: " + modified_by.get_name())
                                                print(
                                                    "Record Attachment Modified By - ID: " + str(modified_by.get_id()))
                                                print(
                                                    "Record Attachment Modified By - Email: " + modified_by.get_email())
                                            print(
                                                "Record Attachment State: " + attachment.get_state())
                                            created_by = attachment.get_created_by()
                                            if created_by is not None:
                                                print(
                                                    "Record Attachment Created By - Name: " + created_by.get_name())
                                                print(
                                                    "Record Attachment Created By - ID: " + str(created_by.get_id()))
                                                print(
                                                    "Record Attachment Created By - Email: " + created_by.get_email())
                                            print(
                                                "Record Attachment LinkUrl: " + str(attachment.get_link_url()))
                                    else:
                                        print(key_name)
                                        for each_value in value:
                                            print(str(each_value))
                            elif isinstance(value, MinifiedUser):
                                print("Record " + key_name +
                                      " User-ID: " + str(value.get_id()))
                                print("Record " + key_name +
                                      " User-Name: " + value.get_name())
                                print("Record " + key_name +
                                      " User-Email: " + value.get_email())
                            elif isinstance(value, MinifiedLayout):
                                print(key_name + " ID: " + str(value.get_id()))
                                print(key_name + " Name: " + value.get_name())
                            elif isinstance(value, Record):
                                print(key_name + " Record ID: " +
                                      str(value.get_id()))
                                print(key_name + " Record Name: ")
                                print(value.get_key_value('name'))
                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())
                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())
                            elif isinstance(value, RecurringActivity):
                                print(key_name)
                                print("RRULE: " + value.get_rrule())
                            elif isinstance(value, Consent):
                                print("Record Consent ID: " +
                                      str(value.get_id()))
                                created_by = value.get_created_by()
                                if created_by is not None:
                                    print(
                                        "Record Consent Created By - Name: " + created_by.get_name())
                                    print(
                                        "Record Consent Created By - ID: " + str(created_by.get_id()))
                                    print(
                                        "Record Consent Created By - Email: " + created_by.get_email())
                                print("Record Consent CreatedTime: " +
                                      str(value.get_created_time()))
                                if value.get_modified_time() is not None:
                                    print("Record Consent ModifiedTime: " +
                                          str(value.get_modified_time()))
                                owner = value.get_owner()
                                if owner is not None:
                                    print(
                                        "Record Consent Created By - Name: " + owner.get_name())
                                    print(
                                        "Record Consent Created By - ID: " + str(owner.get_id()))
                                    print(
                                        "Record Consent Created By - Email: " + owner.get_email())
                                print("Record Consent ContactThroughEmail: " +
                                      str(value.get_contact_through_email()))
                                print("Record Consent ContactThroughSocial: " +
                                      str(value.get_contact_through_social()))
                                print("Record Consent ContactThroughSurvey: " +
                                      str(value.get_contact_through_survey()))
                                print("Record Consent ContactThroughPhone: " +
                                      str(value.get_contact_through_phone()))
                                print("Record Consent MailSentTime: " +
                                      str(value.get_mail_sent_time()))
                                print("Record Consent ConsentDate: " +
                                      str(value.get_consent_date()))
                                print("Record Consent ConsentRemarks: " +
                                      value.get_consent_remarks())
                                print("Record Consent ConsentThrough: " +
                                      value.get_consent_through())
                                print("Record Consent DataProcessingBasis: " +
                                      value.get_data_processing_basis())
                                # To get custom values
                                print("Record Consent Lawful Reason: " +
                                      str(value.get_key_value("Lawful_Reason")))
                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))
                            else:
                                print(key_name + " : " + str(value))
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print('Record Info PerPage: ' +
                                  str(info.get_per_page()))
                        if info.get_page() is not None:
                            print('Record Info Page: ' + str(info.get_page()))
                        if info.get_count() is not None:
                            print('Record Info Count: ' +
                                  str(info.get_count()))
                        if info.get_more_records() is not None:
                            print('Record Info MoreRecords: ' +
                                  str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
GetRecords.initialize()
GetRecords.get_records(module_api_name)
