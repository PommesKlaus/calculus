import React from 'react';
import Numeral from 'numeral';
import { Modal, Button, OverlayTrigger, FormGroup, ControlLabel, FormControl } from 'react-bootstrap';

const AddDifferenceComponent = React.createClass({

  close() {
    this.props.hideModal();
  },

  lineItem() {
    return (this.props.AddToLineItem!==null ? this.props.LineItems.find((x) => x.id===this.props.AddToLineItem).name : this.props.LineItems[0]);
  },

  render() {
    return (
      <div>

        <Modal show={this.props.AddToLineItem!=null} onHide={this.close}>
          <form>
            <Modal.Header closeButton>
              <Modal.Title>Neue HB/StB-Abweichung hinzufügen</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <div className="container-fluid">
                <input type="hidden" name="version_id" value="" />

                <div className="col-md-12">
                  <FormGroup controlId="bs_line_item_id">
                    <ControlLabel>Bilanzposition</ControlLabel>
                    <FormControl componentClass="select">
                      {this.props.LineItems.map(item =>
                        <option value={item.id} selected={item.id===this.props.AddToLineItem ? "selected" : ""}>{item.name}</option>
                      )}
                    </FormControl>
                  </FormGroup>
                </div>

                <div className="col-md-12">
                  <FormGroup controlId="name">
                    <ControlLabel>Bezeichnung der HB/StB-Abweichung</ControlLabel>
                    <FormControl type="text" />
                  </FormGroup>
                </div>

                <div className="col-md-6">
                  <FormGroup controlId="local_gaap">
                    <ControlLabel>Local (HGB-Buchwert)</ControlLabel>
                    <FormControl type="text" />
                  </FormGroup>
                </div>

                <div className="col-md-6">
                  <FormGroup controlId="tax_gaap">
                    <ControlLabel>Tax (StB-Buchwert)</ControlLabel>
                    <FormControl type="text" />
                  </FormGroup>
                </div>

                <div className="col-md-12">
                  <FormGroup controlId="comment">
                    <ControlLabel>Kommentar</ControlLabel>
                    <FormControl componentClass="textarea" placeholder="Kurze Beschreibung zur abweichenden Behandlung in der Steuerbilanz" />
                  </FormGroup>            
                </div>
                
              </div>

            </Modal.Body>
            <Modal.Footer>
              <Button type="submit">Speichern</Button>
              <Button onClick={this.close}>Close</Button>
            </Modal.Footer>
          </form>
        </Modal>
      </div>
    );
  }
});

export default AddDifferenceComponent;
